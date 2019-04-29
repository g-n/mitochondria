using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class gameover : MonoBehaviour
{
    private Renderer rend;
    
    void Start()
    {
        rend = GetComponent<Renderer>();
        rend.material.color = Color.black;
    }

    void OnMouseEnter()
    {
        rend.material.color = Color.green;
    }
    void OnMouseExit()
    {
        rend.material.color = Color.black;
    }
 public void OnMouseUp()
    {
        Time.timeScale = 1;
        SceneManager.LoadScene(0);
    }
}