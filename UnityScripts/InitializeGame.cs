using UnityEngine;
using System;
using TMPro;
using System.Net;
using System.IO;
using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using System.Linq;
using Newtonsoft.Json;

public class InitializeGame : MonoBehaviour
{
    [System.Serializable]
    public class Problem
    {
        public string target;
        public string correct;
        public string incorrect;
    }
    [System.Serializable]
    public class ProblemSet
    {
        public string set_name;
        public Problem[] problems;
        public int id;
    }

    [System.Serializable]
    public class Game
    {
        public string problemset_name;
        public string date;
        public int score;
        public int problemset;
        public int student;
    }
    [System.Serializable]
    public class Game2
    {
        public string date;
        public int score;
        public int problemset;
        public int student;
    }


    [System.Serializable]
    public class Student
    {
        public string first_name;
        public string last_name;
        public Game[] scores;
        public int id;
    }

    public GameObject gutter_prefab;
    public GameObject wall_prefab;
    public GameObject text_prefab;
    public int scalar = 5;
    public string problemset_url;

    public TextMeshProUGUI walls_left;
    public Image speed_value;
    public TextMeshProUGUI target_text;

    public int min_speed = 5;
    public int max_speed = 20;
    public float speed = 10;

    private Rigidbody marble_body;

    int score = 0;
    int num_answered = 0;
    private Problem[] problemset;
    int problemset_len;
    //Item[] problemset;
    GameObject[] left_gutters;
    GameObject[] right_gutters;
    GameObject[] left_walls;
    GameObject[] right_walls;

    string username = GlobalState.username;
    string password = GlobalState.password;
    public string host = GlobalState.host;

    bool[] is_left;
    

    int blocks = 0;


    // z is -10 and +10 for playable space between both walls 
    // len is number of walls and should be a scaler to widen the gap between problems
    // may want to add invisible walls later
    public GameObject[] GenerateGutters(int z, int rot, int len)
    {
        // adjust for Quaternion rotation over 180 degrees to keep centered
        int i = 0;
        if (rot >= 180)
        {
            i = 1;
            len = len + 1;
        }
        GameObject[] gutterarray = new GameObject[len];

        for (; i < len; i++)
        {
            GameObject gutter = Instantiate(gutter_prefab, new Vector3(z, 0, i * 8), Quaternion.Euler(0, rot, 0));
            MeshCollider rb = gutter.AddComponent<MeshCollider>();
            rb.convex = true;
            gutterarray[i] = gutter;
        }
        return gutterarray;
    }

    // len of walls should be equal to number of problems
    public GameObject[] GenerateWalls(int x, int len)
    {
        GameObject[] wallarray = new GameObject[len];

        for (int i = 0; i < len; i++)
        {

            GameObject wall = Instantiate(wall_prefab, new Vector3(x, 2, (i + 1) * 8 * scalar), Quaternion.Euler(90, 0, 0));
            wall.name = "boop";
            wall.layer = LayerMask.NameToLayer("walls");

            wall.transform.localScale += new Vector3(2.9f, 2.9f, 2.9f);
            //Destroy(wall.transform.gameObject.GetComponent<BoxCollider>());
            BoxCollider collider = wall.transform.gameObject.GetComponent<BoxCollider>();
            collider.size = new Vector3(2.5f, 0.5f, 1);
            Rigidbody rb = wall.AddComponent<Rigidbody>();
            rb.useGravity = false;
            wallarray[i] = wall;
        }
        return wallarray;
    }

    // returns a string of unserialized json

     public string AuthRequest(string url)
    {
        HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
        request.Headers.Add("Authorization", "Basic " + System.Convert.ToBase64String(System.Text.Encoding.GetEncoding("ISO-8859-1").GetBytes(username + ":" + password)));
        HttpWebResponse response = (HttpWebResponse)request.GetResponse();
        return new StreamReader(response.GetResponseStream()).ReadToEnd();
    }

    public string AuthUrlRequest(string endpoint, string problemset)
    {
        if (problemset == "" | problemset == null)
        {
            problemset = "easy addition";
        }
        string url = String.Format("{0}{1}/{2}/", host, endpoint, problemset);
        print(url);

        return AuthRequest(url);
    }

    public void AuthPostScore()
    {
        string url = String.Format("{0}/games/", host);
         var request = (HttpWebRequest)WebRequest.Create(url);
        request.Method = "POST";
        request.ContentType = "application/json";
        request.Headers.Add("Authorization", "Basic " + System.Convert.ToBase64String(System.Text.Encoding.GetEncoding("ISO-8859-1").GetBytes(username + ":" + password)));
        string js = JsonConvert.SerializeObject(
            new Game2
            {
                date = String.Format("{0}-{1}-{2}", DateTime.Today.Year, DateTime.Today.Month, DateTime.Today.Day),
            score = this.score,
            problemset = GlobalState.map_id,
            student = GlobalState.user_id
        });
        print(js);

        using (var streamWriter = new StreamWriter(request.GetRequestStream()))
        {
            streamWriter.Write(js);
            streamWriter.Flush();
            streamWriter.Close();
        }

        var httpResponse = (HttpWebResponse)request.GetResponse();
        using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
        {
            var result = streamReader.ReadToEnd();
            print(result);
        }

    }



    public void SetWallsRemaining(int remaining)
    {
        print(remaining);
        walls_left.SetText("<size=70>{0}</size> score", remaining);
    }

    public void SetTargetText(int index)
    {
        target_text.SetText(string.Format("{0}", problemset[index].target));
    }


    public void FillSpeedBar(float min, float max, float current)
    {
        print(String.Format("{0}, {1}, {2}", min, max, current));
        speed_value.fillAmount = ((float)current - min) / (max-min);
    }

    public void ChangeSpeed(int delta)
    {
        float new_speed = speed + delta;
        if (new_speed < min_speed)
        {
            speed = min_speed;
        }
        else if (new_speed > max_speed)
        {
            speed = max_speed;
        }
        else
        {
            speed = new_speed;
        }

        FillSpeedBar(min_speed, max_speed, speed);

    }

    public void SetWallText(GameObject wall, string text, bool is_correct, int index)
    {
        WallData c = wall.AddComponent<WallData>();
        c.correct = is_correct;
        c.index = index;
        Vector3 pos = wall.transform.position + new Vector3(0, 0, -1.1f);
        GameObject txt = Instantiate(text_prefab, pos, Quaternion.Euler(0, 0, 0));
        txt.GetComponent<TextMeshPro>().SetText(text);
        txt.GetComponent<TextMeshPro>().alignment = (TextAlignmentOptions.Center);
    }



    void FixedUpdate()
    {
        float moveHorizontal = Input.GetAxis("Horizontal");
        Vector3 movement = new Vector3(moveHorizontal, 0, 1) * (speed);
        marble_body.velocity = movement;
    }

    void Start()
    {
        SetWallsRemaining(0);
        print(String.Format("map: {0}, id: {1}", GlobalState.map, GlobalState.user_id));

        walls_left = GameObject.Find("WallText").GetComponent<TextMeshProUGUI>();
        speed_value = GameObject.Find("HUD/Speed/Bar/Bar").GetComponent<Image>();
        target_text = GameObject.Find("HUD/Target/TargetText").GetComponent<TextMeshProUGUI>();
        marble_body = GetComponent<Rigidbody>();

        // randomize ordering of problemset
        System.Random rand = new System.Random();
        ProblemSet ps =  JsonConvert.DeserializeObject<ProblemSet>(AuthUrlRequest("/problemsets", GlobalState.map));
        Problem[] it = ps.problems;

        problemset = it.OrderBy(x => rand.Next()).ToArray();

        //update UI elements
        problemset_len = problemset.Length;
        is_left = new bool[problemset_len];
        //SetWallsRemaining(problemset_len);
        SetTargetText(0);
        ChangeSpeed(0);

        //left_gutters = GenerateGutters(-10, 90, problemset_len * scalar);
        //right_gutters = GenerateGutters(10, 270, problemset_len * scalar);

        left_walls = GenerateWalls(-5, problemset_len);
        right_walls = GenerateWalls(5, problemset_len);

        // draw text on walls and shuffle correct answer left or right
        bool[] left_correct = new bool[problemset_len];
        for (int i = 0; i < problemset_len; i++)
        {
            if (rand.Next(0, 2) == 0)
            {
                is_left[i] = true;
                SetWallText(left_walls[i], problemset[i].correct, true, i);
                SetWallText(right_walls[i], problemset[i].incorrect, false, i);
            }
            else
            {
                is_left[i] = false;
                SetWallText(left_walls[i], problemset[i].incorrect, false, i);
                SetWallText(right_walls[i], problemset[i].correct, true, i);
            }
        }
    }
    private void OnTriggerEnter(Collider other)
    {
        GameObject terrain = GameObject.FindGameObjectWithTag("terr");
        Transform t = terrain.transform;
        GameObject t2 = Instantiate(terrain, t.position + t.forward * 300.0f, t.rotation);
        Destroy(terrain, 0);
    }

    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.name.Equals("boop"))
        {
            WallData hit_wall = collision.collider.GetComponent<WallData>();
            if (is_left[hit_wall.index] == true)
            {
                Destroy(left_walls[hit_wall.index].gameObject, 5);
                Destroy(right_walls[hit_wall.index].gameObject.GetComponent<BoxCollider>());
            }
            else
            {
                Destroy(left_walls[hit_wall.index].gameObject.GetComponent<BoxCollider>());
                Destroy(right_walls[hit_wall.index].gameObject, 5);

            }

            print(String.Format("boopest {0} {1}", hit_wall.correct, hit_wall.index));
            num_answered = num_answered + 1;
            int remaining = problemset_len - num_answered;
            //SetWallsRemaining(remaining);
            if (remaining <= 0)
            {

                StartCoroutine(GameOverDelay(3));
            }
            else
            {
                SetTargetText(hit_wall.index + 1);

            }

            if (hit_wall.correct)
            {
                print("correct");
                score = score + 1;
                ChangeSpeed(3);
                SetWallsRemaining(score);
            }
            else
            {
                print("wrong");
                ChangeSpeed(-3);
            }
            left_walls[hit_wall.index].gameObject.name = "answered";
            right_walls[hit_wall.index].gameObject.name = "answered";


        }

    }
    IEnumerator GameOverDelay(float delay)
    {
        yield return new WaitForSeconds(delay);
        print("posting score");
        try
        {
            AuthPostScore();
        } catch {
            print("http error");
        };
        
        SceneManager.LoadScene("Scenes/GameOver");
    }

}
