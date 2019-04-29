using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class StartButton : MonoBehaviour
{
    private Renderer rend;
    // Start is called before the first frame update
    void Start()
    {
        rend = GetComponent<Renderer>();
        rend.material.color = Color.white;
    }

    void OnMouseEnter()
    {
        rend.material.color = Color.red;
    }
    void OnMouseExit()
    {
        rend.material.color = Color.white;
    }
    void OnMouseUp()
    {
        SceneManager.LoadScene("Scenes/Selector");
    }
}
