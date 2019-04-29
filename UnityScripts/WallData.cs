using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WallData : MonoBehaviour
{
    public bool correct;
    public int index;
    public WallData(bool correct, int index)
    {
        this.correct = correct;
        this.index = index;
    }
}
