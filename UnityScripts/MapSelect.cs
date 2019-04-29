using Michsky.UI.Frost;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MapSelect : MonoBehaviour
{
    public string classname = "";
    public string levelname = "";
    public int user_id = -1;
    public int map_id = -1;

    public void LoadClasses()
    {
        print(classname);
         LoadStudents s = GameObject.Find("Main Camera").GetComponent<LoadStudents>();
        s.Page(this.classname);
    }


    public void LoadStudents()
    {
        print(classname);
        LoadStudents s = GameObject.Find("Main Camera").GetComponent<LoadStudents>();
        GlobalState.user_id = this.user_id;
    }

    public void LoadLevel()
    {
        GlobalState.map = this.levelname;
        GlobalState.map_id = this.map_id;
        SceneManager.LoadScene("MainGame");
    }


    void Start()
    {
        TopPanelManager tm = GameObject.Find("Menu Manager").GetComponent<TopPanelManager>();
    }

}
