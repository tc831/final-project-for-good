DROP TABLE IF EXISTS matches_final cascade;

CREATE TABLE matches_final (
"date" DATE, 
"time" VARCHAR, 
"comp" VARCHAR,  
"round" VARCHAR, 
"day" VARCHAR, 
"venue" VARCHAR,  
"result" VARCHAR,  
"gf" INT, 
"ga" INT, 
"opponent"  VARCHAR,   
"xg" FLOAT, 
"xga" FLOAT, 
"poss" INT, 
"attendance" INT, 
"captain" VARCHAR,
"formation" VARCHAR, 
"referee" VARCHAR, 
"match_report" VARCHAR, 
"sh" INT, 
"sot" INT, 
"dist" FLOAT,
"fk" INT, 
"pk" INT, 
"pkatt" INT, 
"season" INT, 
"team" VARCHAR
);

