using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Net;
using UnityEngine;
using Newtonsoft.Json;
using System.Data;
using TMPro;
using UnityEngine.UI;

public class LoadStudents : MonoBehaviour
{
    // Start is called before the first frame update



    public GameObject playerButtonPrefab;

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
        public int problemset_id;
        public int student_id;
    }

    [System.Serializable]
    public class Student
    {
        public string first_name;
        public string last_name;
        public Game[] scores;
        public int id;
    }
    [System.Serializable]
    public class Class
    {
        public Student[] students;
        public string classroom;
    }


    List<Class> classes;
    List<ProblemSet> problemset_names;
    List<GameObject> buttonsRefs;
    List<GameObject> levelRefs;

    public static readonly string host = "http://powerhouseofthecell.herokuapp.com";
    string username = GlobalState.username;
    string password = GlobalState.password;

    void Start()
    {
        print("start!");
        buttonsRefs = new List<GameObject>();
        GameObject listy = GameObject.Find("StudentList");
        GameObject classbutton = GameObject.Find("ClassButton");
        GameObject levelbutton = GameObject.Find("LevelButton");
        levelRefs = new List<GameObject>();
        
        classes = JsonConvert.DeserializeObject<List<Class>>(AuthUrlRequest("/classes"));
        print("classes");
        problemset_names = JsonConvert.DeserializeObject<List<ProblemSet>>(AuthUrlRequest("/problemsets"));
        print("problemsets");

        GameObject e;
        foreach (Class c in classes)
        { 
            e = (GameObject)Instantiate(classbutton);
            e.GetComponentInChildren<TextMeshProUGUI>().SetText(c.classroom);
            e.transform.SetParent(listy.GetComponent<RectTransform>(), true);
            e.GetComponent<RectTransform>().localScale.Set(2, 2, 2);
            e.GetComponent<MapSelect>().classname = c.classroom;
        }

        foreach (ProblemSet s in problemset_names)
        {
            e = (GameObject)Instantiate(levelbutton);
            e.GetComponentInChildren<TextMeshProUGUI>().SetText(s.set_name);
            e.transform.SetParent(GameObject.Find("ChooseLevel").GetComponent<RectTransform>(), true);
            e.GetComponent<RectTransform>().localScale.Set(2, 2, 2);
            e.GetComponent<MapSelect>().levelname = s.set_name;
            e.GetComponent<MapSelect>().map_id = s.id;
            levelRefs.Add(e);
        }

    }

    public void Page(string name)
    {
        print("called");
        GameObject profiles = GameObject.Find("ChooseProfile");
        GameObject userButton = GameObject.Find("UserButtonSmall");
        

        for (int i = 0; i < buttonsRefs.Count; i++)
        {
            Destroy(buttonsRefs[i]);
        }

        GameObject e;    
        foreach (Class c in classes)
        {
            if (c.classroom.Equals(name))
            {
                foreach(Student s in c.students)
                {
                    e = (GameObject)Instantiate(userButton);
                    e.GetComponentInChildren<TextMeshProUGUI>().SetText(String.Format("{0} {1}", s.first_name, s.last_name));
                    e.transform.SetParent(profiles.GetComponent<RectTransform>(), true);
                    e.GetComponent<MapSelect>().user_id = s.id;
                    buttonsRefs.Add(e);

                }

            }
        }
    }

    public string AuthUrlRequest(string endpoint)
    {
        string url = String.Format("{0}{1}/", host,endpoint);
        print(url);
        HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
        request.Headers.Add("Authorization", "Basic " + System.Convert.ToBase64String(System.Text.Encoding.GetEncoding("ISO-8859-1").GetBytes(username + ":" + password)));
        HttpWebResponse response = (HttpWebResponse)request.GetResponse();
        string responseString = new StreamReader(response.GetResponseStream()).ReadToEnd();
        return responseString;
    }
}
