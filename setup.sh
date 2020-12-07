#Flask==1.1.2
#Flask-JWT-Extended==3.25.0
#flask-mongoengine==0.9.5
#Flask-RESTful==0.3.8
#Flask-WTF==0.14.3
#mongoengine==0.20.0

#sudo systemctl start mongod




#82325531-8960-46d8-9b87-8e3857fd8dbc
#df3a73bb-992b-499b-8ab6-c15b154ab2b5
#d6375a1f-1034-4f4a-a178-b8c658068ce9
#5d182908-36ce-4641-846b-46979e1a6a9e
#936aa1a5-c105-4005-9731-c3d712dca5b8
#624bb2e0-55ab-4c46-8f1a-d58c241c0f83
#6ae232de-b5ae-49ac-8da7-1493ba8b6cf7
#fd094f4d-4025-44d4-8148-2029ad25d05e
#ebd5de56-6f72-45e2-9954-7154d262b0a4
#8aeaf7a1-8a23-49cd-bd70-bea61d5840b1
#37dfa461-02c4-441d-8c7f-7cb214de0680
#03f4b221-f875-4b3b-a4c1-cca44cf05627

#b093eca8-be1a-4053-b19e-67c1ac28a42f
#d004f1c9-6937-46fc-a499-8eaba2cb9d38
#131a0edd-73a6-410e-b72e-ce86db48530f
#e82f39ba-5d3a-43e7-9647-5fe07d9d481a
#ba5a75ad-0ce3-475f-88e8-0b73ce5f3e38
#ed16b5e5-2aee-4814-a023-7851f9fe245e
#7c863d7f-fe55-4ce4-85ac-c1f5e806980c
#706c337a-7331-4c5f-b7db-ac6b1417266a
#a26c4776-1960-45dd-b183-4a9d8c942228
#334ed732-adc4-4519-9f09-17288463a533
#960adf8e-425c-46b5-91c4-59d34573d8e4
#45e5b17e-e43b-4796-810a-359274fdda5c
#666538aa-9ff3-4539-af85-c936c25ef60f
#e44a049e-223d-4cd7-869a-501114ffaed4
#3d517fbf-6924-48c4-96e7-f38ed2031cc9
#85db188c-f911-4a8f-8347-ea5b12aae77b
#ad0e6b48-7076-4df3-b1e1-20dc201b3340
#f6262e8b-580c-4e0a-8acf-b66392e62bc6
#40050f34-8606-407a-982a-0083cfa9a987
#9b52e679-52b3-483b-97d8-7d91efc1e0d4
#c2166d3d-08ef-4a3e-87c8-f1de9ef6483c
#b3bd8f56-573a-413b-a6b6-b6c0a32cf2db
#27de0977-a3dc-4201-a898-2b4dd24dd2ca
#58424a45-3af8-46b8-adaf-a7e482657a2b
#89300003-166e-4730-95d3-ea69db50bcec
#eebf791c-6890-4c91-a07c-f7554fde6b1c
#5ba08880-816f-43c7-8dd5-d7324d1a2a94
#165c6d9e-d9f8-40f5-8de1-77314ea5ac16
#265e2cd1-084b-406c-83c5-d72eb00fa5a8
#aef2084b-2dbb-49e4-9c29-8254e5d656a7
#92407928-7fea-4c92-a8e6-8f9982d48722
#efee06e8-82f5-4208-83d5-76b1583a0532
#ca45b31b-4948-41b1-829b-1a2b2a08bb6c
#734be512-fc14-4b04-9556-57248bcaa8f6
#9a6ea519-7a34-4c2d-9efa-bd8d079a14a3
#7f32efa5-6fb7-4dfb-95f5-e8f0f7945474
#61c7e8cb-29f6-4291-874e-7425a80a9c79
#8f37248a-1400-414f-be44-6c9669176076
#1edc411f-e97b-4720-ac2c-e7c4f702c308
#1ef0dcdb-495a-494e-aba5-6936dc2ba43b
#e2b03d76-3f64-448a-9e4b-deebd8183f7e
#fbeb2687-9d86-4edc-912c-9095a76ab5eb
#a83653c6-ecfc-47e4-b3ac-670c9ef17115
#3282feb9-cd6c-4fd4-a2d4-362d5ef02c2e
#8b14ab35-ca82-4bb5-8b49-b18c1ae12ec6
#96672eed-7d2c-45b2-a12d-9bb954270f7d
#e2ae3cc3-8d0c-4e6e-805b-e702479262df
#fdf345a4-54b7-4068-9657-0a744cfe310c
#47ad67a2-b61c-4588-b0c0-a8de1451fbba
#6a80422a-7eed-4870-b005-95f8eae61ef5
#b35277a6-86ec-4d00-a179-0adade88c1d4



curl --location --request DELETE 'http://127.0.0.1:5000/reset'


curl --location --request POST 'http://127.0.0.1:5000/location' \
--header 'Content-Type: application/json' \
--data-raw '{
    "location_id": "d16b522e-b999-4374-aefc-d6070e07e125",
    "city": "Santa Clara",
    "state": "CA",
    "country": "United States",
    "zipcode": 95056,
    "latitude": 6,
    "longitude":  6
}'

curl --location --request POST 'http://127.0.0.1:5000/location' \
--header 'Content-Type: application/json' \
--data-raw '{
    "location_id": "2797943a-10ba-4487-a32b-528d03f16534",
    "city": "Santa Clara",
    "state": "CA",
    "country": "United States",
    "zipcode": 95055,
    "latitude": 5,
    "longitude":  5
}'

curl --location --request POST 'http://127.0.0.1:5000/location' \
--header 'Content-Type: application/json' \
--data-raw '{
    "location_id": "701d4aec-5343-40fa-a48c-15926c89e445",
    "city": "Santa Clara",
    "state": "CA",
    "country": "United States",
    "zipcode": 95054,
    "latitude": 4,
    "longitude":  4
}'

curl --location --request POST 'http://127.0.0.1:5000/location' \
--header 'Content-Type: application/json' \
--data-raw '{
    "location_id": "52a56d15-71f3-4dde-acc5-6409d0a8498d",
    "city": "Santa Clara",
    "state": "CA",
    "country": "United States",
    "zipcode": 95053,
    "latitude": 3,
    "longitude":  3
}'

curl --location --request POST 'http://127.0.0.1:5000/location' \
--header 'Content-Type: application/json' \
--data-raw '{
    "location_id": "8c996e24-ea58-4f57-9315-4ee6c8852591",
    "city": "Santa Clara",
    "state": "CA",
    "country": "United States",
    "zipcode": 95052,
    "latitude": 2,
    "longitude":  2
}'

curl --location --request POST 'http://127.0.0.1:5000/location' \
--header 'Content-Type: application/json' \
--data-raw '{
    "location_id": "3c3a7218-e1b9-4e70-bfe4-08f276e5f279",
    "city": "Santa Clara",
    "state": "CA",
    "country": "United States",
    "zipcode": 95051,
    "latitude": 1,
    "longitude":  1
}'



curl --location --request POST 'http://127.0.0.1:5000/student/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "student_id": "e3f1c7ab-5511-42cf-bf6c-3245fd13ad56",
    "email": "student1",
    "username": "student1",
    "password": "student1",
    "fname": "Student1",
    "lname": "Student1",
    "city": "Santa Clara",
    "state": "CA",
    "zipcode": 95051
}'


curl --location --request POST 'http://127.0.0.1:5000/student/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "student_id": "e0577a78-5c9e-46f3-a776-941537645341",
    "email": "student2",
    "username": "student2",
    "password": "student2",
    "fname": "Student2",
    "lname": "Student2",
    "city": "Santa Clara",
    "state": "CA",
    "zipcode": 95052
}'

curl --location --request POST 'http://127.0.0.1:5000/student/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "student_id": "6b8478ab-3e7d-4ca8-9524-25458fa47f14",
    "email": "student3",
    "username": "student3",
    "password": "student3",
    "fname": "Student3",
    "lname": "Student3",
    "city": "Santa Clara",
    "state": "CA",
    "zipcode": 95053
}'

curl --location --request POST 'http://127.0.0.1:5000/student/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "student_id": "afe4aaa8-eea8-4435-8553-28a7745007a9",
    "email": "student4",
    "username": "student4",
    "password": "student4",
    "fname": "Student4",
    "lname": "Student4",
    "city": "Santa Clara",
    "state": "CA",
    "zipcode": 95054
}'



curl --location --request POST 'http://127.0.0.1:5000/instructor/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "instructor_id": "0d2250a2-c44c-41dc-befe-f1c5f348aacc",
    "email": "instructor1",
    "username": "instructor1",
    "password": "instructor1",
    "fname": "Instructor1",
    "lname": "Instructor1",
    "city": "Santa Clara",
    "state": "CA",
    "zipcode": 95051
}'


curl --location --request POST 'http://127.0.0.1:5000/instructor/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "instructor_id": "7e66a15e-4e46-48a6-b63d-51377802b3e7",
    "email": "instructor2",
    "username": "instructor2",
    "password": "instructor2",
    "fname": "Instructor2",
    "lname": "Instructor2",
    "city": "Santa Clara",
    "state": "CA",
    "zipcode": 95052
}'


curl --location --request POST 'http://127.0.0.1:5000/instructor/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "instructor_id": "721f0c77-1ecb-47c7-a62d-93e923e02f8b",
    "email": "instructor3",
    "username": "instructor3",
    "password": "instructor3",
    "fname": "Instructor3",
    "lname": "Instructor3",
    "city": "Santa Clara",
    "state": "CA",
    "zipcode": 95053
}'


curl --location --request POST 'http://127.0.0.1:5000/instructor/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "instructor_id": "20f5e9f6-1a96-45ee-b7fb-34d75c549a7f",
    "email": "instructor4",
    "username": "instructor4",
    "password": "instructor4",
    "fname": "Instructor4",
    "lname": "Instructor4",
    "city": "Santa Clara",
    "state": "CA",
    "zipcode": 95054
}'



curl --location --request POST 'http://127.0.0.1:5000/class' \
--header 'Content-Type: application/json' \
--data-raw '{
    "description": "class1",
    "class_level": 1,
    "format": "OFFLINE",
    "duration": 60,
    "class_cost": 20,
    "instructor_id": "20f5e9f6-1a96-45ee-b7fb-34d75c549a7f",
    "location_id": "701d4aec-5343-40fa-a48c-15926c89e445",
    "class_id": "3a7f2cbf-51cc-4cfb-8d9c-cbf6ee670f7e"

}'

curl --location --request POST 'http://127.0.0.1:5000/class' \
--header 'Content-Type: application/json' \
--data-raw '{
    "description": "class1",
    "class_level": 1,
    "format": "OFFLINE",
    "duration": 60,
    "class_cost": 20,
    "instructor_id": "721f0c77-1ecb-47c7-a62d-93e923e02f8b",
    "location_id": "701d4aec-5343-40fa-a48c-15926c89e445",
    "class_id": "f681dfb4-0555-4013-aaac-4545ffba8a87"

}'


curl --location --request POST 'http://127.0.0.1:5000/class' \
--header 'Content-Type: application/json' \
--data-raw '{
    "description": "class1",
    "class_level": 1,
    "format": "OFFLINE",
    "duration": 60,
    "class_cost": 20,
    "instructor_id": "7e66a15e-4e46-48a6-b63d-51377802b3e7",
    "location_id": "701d4aec-5343-40fa-a48c-15926c89e445",
    "class_id": "44b17d5b-21f0-485b-8aa6-c5b4435a5397"
}'


curl --location --request POST 'http://127.0.0.1:5000/class' \
--header 'Content-Type: application/json' \
--data-raw '{
    "description": "class1",
    "class_level": 1,
    "format": "OFFLINE",
    "duration": 60,
    "class_cost": 20,
    "instructor_id": "0d2250a2-c44c-41dc-befe-f1c5f348aacc",
    "location_id": "701d4aec-5343-40fa-a48c-15926c89e445",
    "class_id": "9561c85d-27b2-4c58-8941-43ade8b779fc"
}'


curl --location --request POST 'http://127.0.0.1:5000/class' \
--header 'Content-Type: application/json' \
--data-raw '{
    "description": "class2",
    "class_level": 2,
    "format": "OFFLINE",
    "duration": 90,
    "class_cost": 20,
    "instructor_id": "20f5e9f6-1a96-45ee-b7fb-34d75c549a7f",
    "location_id": "d16b522e-b999-4374-aefc-d6070e07e125",
    "class_id": "afd0b178-f416-4c19-83ab-f32cf3522f5d"

}'

curl --location --request POST 'http://127.0.0.1:5000/class' \
--header 'Content-Type: application/json' \
--data-raw '{
    "description": "class2",
    "class_level": 2,
    "format": "OFFLINE",
    "duration": 90,
    "class_cost": 20,
    "instructor_id": "721f0c77-1ecb-47c7-a62d-93e923e02f8b",
    "location_id": "d16b522e-b999-4374-aefc-d6070e07e125",
    "class_id": "0ae7502e-ecf2-495a-94ba-08f9395e5f79"

}'


curl --location --request POST 'http://127.0.0.1:5000/class' \
--header 'Content-Type: application/json' \
--data-raw '{
    "description": "class2",
    "class_level": 2,
    "format": "OFFLINE",
    "duration": 90,
    "class_cost": 20,
    "instructor_id": "7e66a15e-4e46-48a6-b63d-51377802b3e7",
    "location_id": "d16b522e-b999-4374-aefc-d6070e07e125",
    "class_id": "94434e58-a7f4-4eae-9925-f10d6a9ad958"
}'


curl --location --request POST 'http://127.0.0.1:5000/class' \
--header 'Content-Type: application/json' \
--data-raw '{
    "description": "class2",
    "class_level": 2,
    "class_count": 2,
    "duration": 90,
    "class_cost": 20,
    "instructor_id": "0d2250a2-c44c-41dc-befe-f1c5f348aacc",
    "location_id": "d16b522e-b999-4374-aefc-d6070e07e125",
    "class_id": "62d2b0f7-02a1-475f-a1ec-2a5e0f83b00d"
}'

curl --location --request POST 'http://127.0.0.1:5000/offer' \
--header 'Content-Type: application/json' \
--data-raw '{
    "description": "offer1",
    "value": 2,
    "max_count": 1,
    "currency": "USD",
    "instructor_id": "0d2250a2-c44c-41dc-befe-f1c5f348aacc",
    "class_id": "62d2b0f7-02a1-475f-a1ec-2a5e0f83b00d",
    "offer_id": "975b89a5-6249-4425-93a0-385c96484ee6"
}'

curl --location --request POST 'http://127.0.0.1:5000/offer' \
--header 'Content-Type: application/json' \
--data-raw '{
    "description": "offer2",
    "value": 1,
    "max_count": 3,
    "currency": "USD",
    "instructor_id": "0d2250a2-c44c-41dc-befe-f1c5f348aacc",
    "offer_id": "6bef973a-0ebe-463a-881d-85c2de368504"
}'

curl --location --request POST 'http://127.0.0.1:5000/offer' \
--header 'Content-Type: application/json' \
--data-raw '{
    "description": "offer3",
    "value": 2,
    "max_count": 1,
    "currency": "USD",
    "instructor_id": "7e66a15e-4e46-48a6-b63d-51377802b3e7",
    "class_id": "94434e58-a7f4-4eae-9925-f10d6a9ad958",
    "offer_id": "c5cfc9f0-7ab3-472f-85a8-610a43a99455"
}'

curl --location --request POST 'http://127.0.0.1:5000/offer' \
--header 'Content-Type: application/json' \
--data-raw '{
    "description": "offer4",
    "value": 1,
    "max_count": 3,
    "currency": "USD",
    "instructor_id": "7e66a15e-4e46-48a6-b63d-51377802b3e7",
    "offer_id": "ca1a5447-d6e7-4a17-9620-1e2f462f3e27"
}'


curl --location --request POST 'http://127.0.0.1:5000/offer' \
--header 'Content-Type: application/json' \
--data-raw '{
    "description": "offer3",
    "value": 2,
    "max_count": 1,
    "currency": "USD",
    "instructor_id": "721f0c77-1ecb-47c7-a62d-93e923e02f8b",
    "class_id": "0ae7502e-ecf2-495a-94ba-08f9395e5f79",
    "offer_id": "89611cf4-c257-4e06-8ed8-66bd9cfa8394"
}'

curl --location --request POST 'http://127.0.0.1:5000/offer' \
--header 'Content-Type: application/json' \
--data-raw '{
    "description": "offer4",
    "value": 1,
    "max_count": 3,
    "currency": "USD",
    "instructor_id": "721f0c77-1ecb-47c7-a62d-93e923e02f8b",
    "offer_id": "86a5eab5-55da-4d5d-8e25-02b4f880fd17"
}'


curl --location --request POST 'http://127.0.0.1:5000/class-session' \
--header 'Content-Type: application/json' \
--data-raw '{
    "count": 1,
    "student_id": "6b8478ab-3e7d-4ca8-9524-25458fa47f14",
    "class_id": "f681dfb4-0555-4013-aaac-4545ffba8a87",
    "offer_id": "86a5eab5-55da-4d5d-8e25-02b4f880fd17",
    "class_session_id": "b3cb787c-f769-402b-b08a-79def45f330d",
    "offer_usage_id": "9aada7c7-ecfd-4ff2-86a7-681800e2ca20"
}'


curl --location --request POST 'http://127.0.0.1:5000/class-session' \
--header 'Content-Type: application/json' \
--data-raw '{
    "count": 1,
    "student_id": "6b8478ab-3e7d-4ca8-9524-25458fa47f14",
    "class_id": "f681dfb4-0555-4013-aaac-4545ffba8a87",
    "offer_id": "86a5eab5-55da-4d5d-8e25-02b4f880fd17",
    "class_session_id": "b3cb787c-f769-402b-b08a-79def45f330d",
    "offer_usage_id": "9aada7c7-ecfd-4ff2-86a7-681800e2ca20"
}'

curl --location --request POST 'http://127.0.0.1:5000/class-session' \
--header 'Content-Type: application/json' \
--data-raw '{
    "count": 1,
    "student_id": "6b8478ab-3e7d-4ca8-9524-25458fa47f14",
    "class_id": "0ae7502e-ecf2-495a-94ba-08f9395e5f79",
    "offer_id": "86a5eab5-55da-4d5d-8e25-02b4f880fd17",
    "class_session_id": "20285903-dee7-46cb-a2b8-180bf3d95a6f",
    "offer_usage_id": "2c01f86d-037e-433c-9e6b-24843720e078"
}'

curl --location --request POST 'http://127.0.0.1:5000/class-session' \
--header 'Content-Type: application/json' \
--data-raw '{
    "count": 1,
    "student_id": "6b8478ab-3e7d-4ca8-9524-25458fa47f14",
    "class_id": "94434e58-a7f4-4eae-9925-f10d6a9ad958",
    "offer_id": "86a5eab5-55da-4d5d-8e25-02b4f880fd17",
    "class_session_id": "ec1d2899-1da4-4b4e-be93-d50ce764035b",
    "offer_usage_id": "037d3171-2a44-4607-826c-a9e27d9d6b36"
}'

curl --location --request POST 'http://127.0.0.1:5000/class-session' \
--header 'Content-Type: application/json' \
--data-raw '{
    "count": 1,
    "student_id": "6b8478ab-3e7d-4ca8-9524-25458fa47f14",
    "class_id": "44b17d5b-21f0-485b-8aa6-c5b4435a5397",
    "offer_id": "86a5eab5-55da-4d5d-8e25-02b4f880fd17",
    "class_session_id": "ec1d2899-1da4-4b4e-be93-d50ce764035b",
    "offer_usage_id": "037d3171-2a44-4607-826c-a9e27d9d6b36"
}'


curl --location --request GET 'http://127.0.0.1:5000/class-session?location=701d4aec534340faa48c15926c89e445' \
--header 'Content-Type: application/json' \
--data-raw '{
    "count": 1,
    "student_id": "6b8478ab-3e7d-4ca8-9524-25458fa47f14",
    "class_id": "f681dfb4-0555-4013-aaac-4545ffba8a87",
    "offer_id": "86a5eab5-55da-4d5d-8e25-02b4f880fd17",
    "class_session_id": "b3cb787c-f769-402b-b08a-79def45f330d",
    "offer_usage_id": "9aada7c7-ecfd-4ff2-86a7-681800e2ca20"
}'

