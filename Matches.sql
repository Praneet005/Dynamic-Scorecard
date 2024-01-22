use icc_cwc;

create table matches(
	wc_event varchar(50),
    wc_round varchar(50),
    match_no int,
    match_date datetime,
    venue varchar(200),
    city varchar(50),
    team1 varchar(50),
    team2 varchar(50),
    winner varchar(20),
    primary key (match_no)
    
    );
