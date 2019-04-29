using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
public class PlayerController : MonoBehaviour
{
    public float speed;
    private Rigidbody rb;
	public Text CorrectAnwer;
	public GameObject ContinuePanel;

    public bool paused;
    public Text resumePause = null;
    void Start()
    {
		i=1;
        rb = GetComponent<Rigidbody>();
        paused = false;
    }


    public void Pause()
    {
        paused = !paused;
        if (paused)
        {
            resumePause.text = "Resume";
            Time.timeScale = 0;
        }
        else if (!paused)
        {
            resumePause.text = "Pause";
            Time.timeScale = 1;
        }
    }


    void FixedUpdate()
    {
		//Debug.Log(i);
        float moveHorizontal = Input.GetAxis("Horizontal");
        //float moveVertical = Input.GetAxis("Vertical");
        Vector3 movement = new Vector3(moveHorizontal, 0, 1) * speed;
        //rb.AddForce(movement * speed);
        rb.velocity = movement;
    }
	public static int i=1;
    void OnCollisionEnter(Collision other)
    {
		if(other.gameObject.CompareTag("RightAnswer")){

			i++;
		}

     else if (other.gameObject.CompareTag("WrongAnswer"))
        {

			ContinuePanel.SetActive(true);

			if(i==1){
				CorrectAnwer.text="Correct Answer is: 5";
			}
			if(i==2){
				CorrectAnwer.text="Correct Answer is: 8";
			}
			if(i==3){
				CorrectAnwer.text="Correct Answer is: 20";
			}
			if(i==4){
				CorrectAnwer.text="Correct Answer is: 5";
			}
			if(i==5){
				CorrectAnwer.text="Correct Answer is: 8";
			}
			if(i==6){
				CorrectAnwer.text="Correct Answer is: 20";
			}
			i++;
			 Time.timeScale = 0;
            // other.gameObject.SetActive(false);
          
        }
      //  else
      //  {
      
            //SceneManager.LoadScene("GameOver");
       // }
    }
	public void ContinueBtn(){
		SceneManager.LoadScene(2);
		i=1;
		Time.timeScale = 1;
	}
}


