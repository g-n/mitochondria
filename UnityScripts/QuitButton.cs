using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.SceneManagement;

public class QuitButton : MonoBehaviour
{
    private Renderer render;
    // Start is called before the first frame update
    void Start()
    {
        render = GetComponent<Renderer>();
        render.material.color = Color.white;
    }

    void OnMouseEnter()
    {
        render.material.color = Color.red;
    }
    void OnMouseExit()
    {
        render.material.color = Color.white;
    }
    void OnMouseUp()
    {
        SceneManager.LoadScene("Scenes/StartPage");

    }
}
