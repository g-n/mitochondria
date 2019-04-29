using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour
{

    public float FollowDistance = 30.0f;
    private Transform cameraTransform;
    public Transform CameraTarget;

    void Awake()
    {
        cameraTransform = transform;
    }

    void LateUpdate()
    {
        Vector3 t = CameraTarget.position;
        t.Set(0, t.y, t.z);

        cameraTransform.position = CameraTarget.position + new Vector3(-CameraTarget.position.x, 3, -FollowDistance);
        cameraTransform.LookAt(t);
    }
}
