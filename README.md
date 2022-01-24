# **AJS by AlexZai007**


![Снимок экрана 2022-01-24 200222](https://user-images.githubusercontent.com/52669201/150830496-8960db41-6d99-4f65-865d-2fe9f42e08a2.png)

## **A little bit about ajs**

This app is made for students by students. Those who physically cannot wake up early in the morning, those who just want to eat or sleep more.


Our application was created specifically for the convenience and proper distribution of your personal time. If you are a student and you study remotely, but you were the first to set up physical education and you don’t want to wake up, then AJR will help you out! Just enter the time and link next, our application will do everything for you

## How to use?

### **1**. **to get started, go to mos.ru and get a link to the lesson activation page**



go to your diary
![Снимок экрана 2022-01-24 201935](https://user-images.githubusercontent.com/52669201/150833240-132a0a12-0edb-4d91-b138-ccf7c27bead5.png)
here you can see the time of the lessons, add it to the config. And go to one of the lessons
![Снимок экрана 2022-01-24 202013](https://user-images.githubusercontent.com/52669201/150833248-a7b3d8a3-0ef1-46e5-a3b1-672a0617bd6f.png)
here you see a link that the program should accept and the time of the beginning and end of the lesson (DO NOT FORGET TO ENTER THEM IN THE CONFIG)
![Снимок экрана 2022-01-24 202030](https://user-images.githubusercontent.com/52669201/150833250-dab528e6-73cb-40e5-ba9c-d453e154e422.png)


this is an example of how the block should look like with url and start and end times of lessons

```
u_1 = ("https://dnevnik.mos.ru/diary/diary/lessons/294460487_normal")
u_2 = ("https://dnevnik.mos.ru/diary/diary/lessons/282600729_normal")
u_3 = ("https://dnevnik.mos.ru/diary/diary/lessons/282600706_normal")
u_4 = ("https://dnevnik.mos.ru/diary/diary/lessons/282600721_normal")
u_5 = ("https://dnevnik.mos.ru/diary/diary/lessons/282600733_normal")
u_6 = ("https://dnevnik.mos.ru/diary/diary/lessons/282600734_normal")
u_7 = ("0")
u_8 = ("0")

t_1 = ["8:30", "19:15"]
t_2 = ["9:30", "10:15"]
t_3 = ["10:35", "11:20"]
t_4 = ["11:35", "12:20"]
t_5 = ["12:35", "13:20"]
t_6 = ["13:45", "14:25"]
t_7 = ["0", "0"]
t_8 = ["0", "0"]

```

### **2. Specify coordinates**
Specify the coordinates in the config, the table of contents is written.
how to get coordinates? We tinkered about it and wrote a utility.


Go to Utilities
![Снимок экрана 2022-01-24 203324](https://user-images.githubusercontent.com/52669201/150834617-91bcf3c6-91f3-4e7a-a89d-269ed3d82209.png)


run the .bat file
![Снимок экрана 2022-01-24 203334](https://user-images.githubusercontent.com/52669201/150834639-9ff1dfa2-5184-4006-9d34-21f012a3a42d.png)


hover over the button that is written in the configs


Next, you will see coordinates in a separate window
![Снимок экрана 2022-01-24 203352](https://user-images.githubusercontent.com/52669201/150834688-b764457e-d25a-491c-8c50-87952a246d6c.png)

Write them to the general config

```
#кнопка (открыть приложение "Microsoft Teams")
b_x_open = 2214
b_y_open = 503

#кнопка (Присоедениться к уроку)
b_x_join = 2584
b_y_join = 1006

#кнопка (Присоедениться сейчас в тимс)
b_x_join_inapp = 2267
b_y_join_inapp = 1269

#кнопка (Присоедениться сейчас в тимс)
b_x_leave_inapp = 4058
b_y_leave_inapp = 126
```


### **3. Delay Variable**

It would seem one small line, but how much does it mean. This variable is responsible for the delay between any transitions in the browser.

Study the results of the study and take into account the larger the number, the longer you will be absent from the lesson


| Status        | Parameter          | 
| ------------- |:------------------:| 
| GREAT         |        0-5         | 
| LESS EXCELLENT|        5-10        | 
| THE AVERAGE   |        15-30       |
| BADLY         |        30-60       | 
| TERRIBLE      |        60-120      |




Thank you for choosing us. We can not only help but also surprise with the simplicity of the solution. AJS by alexzai007
