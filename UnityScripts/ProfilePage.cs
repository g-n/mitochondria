using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Net;
using UnityEngine;
using UnityEngine.UI;

public class ProfilePage : MonoBehaviour
{
    [System.Serializable]
    public class Profile
    {
        public StudentsScoreProfile[] result;
    }

    [System.Serializable]
    public class StudentsScoreProfile
    {
        public Students[] students;
        public string classroom;
    }

    [System.Serializable]
    public class Students
    {
        public string first_name;
        public string last_name;
        public Score[] scores;
        public int id;
    }

    [System.Serializable]
    public class Score
    {
        public string problemset_name;
        public string date;
        public int score;
        public int problemset;
        public int student;
    }

    public GameObject[] studentInf;
    //private int scoreRate;
    public Profile RequestStudentProfile(string url)
    {
        // currently there is no way to select more than 1 student at a time from a URL
        //HttpWebRequest request = (HttpWebRequest) WebRequest.Create(url);
        ////request.Headers = 
        //HttpWebResponse response = (HttpWebResponse)request.GetResponse();
        //string responseString = new StreamReader(response.GetResponseStream()).ReadToEnd();
        
        //Student student = JsonUtility.FromJson<Student>(responseString);
        //return student;

        HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
        request.Credentials = new NetworkCredential("username", "password");

        string credidentials = "teacher:teacher";
        string authorization = System.Convert.ToBase64String(System.Text.Encoding.Default.GetBytes(credidentials));
        request.Headers["Authorization"] = "Basic " + authorization;

        HttpWebResponse response = (HttpWebResponse)request.GetResponse();
        string responseString = new StreamReader(response.GetResponseStream()).ReadToEnd();
        responseString = "{\"result\":" + responseString + "}";
        Profile profile = JsonUtility.FromJson<Profile>(responseString);
        return profile;

    }

    void Start()
    {
        //scoreRate = 0;
        string url = "https://powerhouseofthecell.herokuapp.com/classes/";
        //Debug.Log(RequestStudentProfile(url));

        //Student test_student = RequestStudentProfile(url);
        //print(string.Format("first_name: {0} last_name: {1}", test_student.first_name, test_student.last_name));
        ResultShow();
    }

    void Update()
    {
        
    }

    void ResultShow() {
        Profile profileInf = RequestStudentProfile("https://powerhouseofthecell.herokuapp.com/classes/");
        
        int nID = 0, nSt, i, j;
        int nStudents = 0;
        for(i=0; i< profileInf.result.Length; i++ )
            nStudents += profileInf.result[i].students.Length;

        for (i = 0; i < profileInf.result.Length; i++) {
            int nSumRate = 0;
            nSt = nID;
            for (j = 0; j < profileInf.result[i].students.Length; j++) {
                // ID for No (Student)
                studentInf[nID].gameObject.transform.Find("No").GetComponentInChildren<Text>().text
                                                                            = profileInf.result[i].students[j].id.ToString();
                // ID for FirstName (Student)
                studentInf[nID].gameObject.transform.Find("FirstName").GetComponentInChildren<Text>().text
                    = profileInf.result[i].students[j].first_name;

                // Id for LastName (Student)
                studentInf[nID].gameObject.transform.Find("LastName").GetComponentInChildren<Text>().text
                    = profileInf.result[i].students[j].last_name;

                int nScoreSum = 0;
                //Id for Score (Student)
                if (profileInf.result[i].students[j].scores.Length > 0) {
                    for (int k = 0; k < profileInf.result[i].students[j].scores.Length; k++)
                        nScoreSum += profileInf.result[i].students[j].scores[k].score;
                    /*
                    studentInf[profileInf.result[i].students[j].id - 1].gameObject.transform.FindChild("Score").GetComponentInChildren<Text>().text
                     = profileInf.result[i].students[j].scores[profileInf.result[i].students[j].scores.Length - 1].score.ToString();

                    //Id for Correct Rate  (Student)
                    for (int k = 0; k < profileInf.result[i].students[j].scores.Length; k++)
                        scoreRate += profileInf.result[i].students[j].scores[k].score;

                    scoreRate = scoreRate / profileInf.result[i].students[j].scores.Length * 20;
                    studentInf[profileInf.result[i].students[j].id - 1].gameObject.transform.FindChild("Correct Rate").GetComponentInChildren<Text>().text
                        = scoreRate.ToString();
                        */
                    int score = nScoreSum / profileInf.result[i].students[j].scores.Length;
                    studentInf[nID].gameObject.transform.Find("Score").GetComponentInChildren<Text>().text
                         = score.ToString();
                    nSumRate += score;
                }

                //scoreRate = 0;
                // Id for ClassRoom  (Student)
                studentInf[nID].gameObject.transform.Find("ClassRoom").GetComponentInChildren<Text>().text
                    = profileInf.result[i].classroom;

                nID ++;
            }

            for ( j = 0; j < profileInf.result[i].students.Length; j++, nSt++ )
            {
                if(profileInf.result[i].students[j].scores.Length > 0)
                    studentInf[nSt].gameObject.transform.Find("Correct Rate").GetComponentInChildren<Text>().text
                                    = (int.Parse(studentInf[nSt].gameObject.transform.Find("Score").GetComponentInChildren<Text>().text)* 100 / nStudents).ToString()+"%";

            }

        }        
    }
}

