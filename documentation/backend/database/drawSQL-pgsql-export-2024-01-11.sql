CREATE TABLE "workout"(
    "id" BIGINT NOT NULL,
    "day" BIGINT NOT NULL
);
ALTER TABLE
    "workout" ADD PRIMARY KEY("id");
CREATE TABLE "user"(
    "id" BIGINT NOT NULL,
    "username" CHAR(255) NOT NULL,
    "email" CHAR(255) NOT NULL,
    "password" CHAR(255) NOT NULL
);
ALTER TABLE
    "User" ADD PRIMARY KEY("id");
CREATE TABLE "sets"(
    "id" BIGINT NOT NULL,
    "exercise" BIGINT NOT NULL,
    "reps" BIGINT NOT NULL,
    "weight" BIGINT NOT NULL
);
ALTER TABLE
    "sets" ADD PRIMARY KEY("id");
CREATE TABLE "exercise"(
    "id" BIGINT NOT NULL,
    "workout" BIGINT NOT NULL,
    "name" CHAR(255) NOT NULL
);
ALTER TABLE
    "exercises" ADD PRIMARY KEY("id");
CREATE TABLE "day"(
    "id" BIGINT NOT NULL,
    "user" BIGINT NOT NULL
);
ALTER TABLE
    "Day" ADD PRIMARY KEY("id");
ALTER TABLE
    "workout" ADD CONSTRAINT "workout_day_foreign" FOREIGN KEY("day") REFERENCES "day"("id");
ALTER TABLE
    "Day" ADD CONSTRAINT "day_user_foreign" FOREIGN KEY("user") REFERENCES "user"("id");
ALTER TABLE
    "sets" ADD CONSTRAINT "sets_exercise_foreign" FOREIGN KEY("exercise") REFERENCES "exercises"("id");
ALTER TABLE
    "exercises" ADD CONSTRAINT "exercises_workout_foreign" FOREIGN KEY("workout") REFERENCES "workout"("id");