use icc_cwc;

create table scores(
	s_no int,
    match_no int,
    batting varchar(50),
    innings int,
    over_no float,
    batsman varchar(50),
    bowler varchar(50),
    non_striker varchar(50),
    bat_score int,
    ext_score int,
    ext_bool varchar(10),
    extras varchar(50),
    wkt_type varchar(50),
    wkt_bool varchar(10),
    player_out varchar(50),
    run_total int,
    wicket_count int,
    primary key (s_no),
    foreign key (match_no) references matches(match_no)
    );
    
