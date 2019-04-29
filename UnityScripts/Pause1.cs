using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;

public class Pause1 : MonoBehaviour
{

    private float cur_speed = 0;
    InitializeGame player;

    private void Awake()
    {
        player = GameObject.FindGameObjectWithTag("Player").GetComponent<InitializeGame>();

    }
    private void OnEnable()
    {
        cur_speed = player.speed;
        player.speed = 0;
    }
    private void OnDisable()
    {
        player.speed = cur_speed;
    }
}
