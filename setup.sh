





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

