using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class replay : MonoBehaviour
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
        SceneManager.LoadScene("Scenes/MainGame");
    }
}
