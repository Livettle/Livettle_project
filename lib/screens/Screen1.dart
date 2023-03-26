import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';
import 'package:sdgplivettle/screens/toprated.dart';
import 'package:sdgplivettle/screens/trending.dart';
import 'package:sdgplivettle/screens/tv.dart';
import 'package:tmdb_api/tmdb_api.dart';

class ScreenOne extends StatefulWidget {
  const ScreenOne({super.key});

  @override
  State<ScreenOne> createState() => _ScreenOneState();
}

class _ScreenOneState extends State<ScreenOne> {
  List trendingmovies = [];
  List topratedmovies = [];
  List tv = [];
  final String apikey = '845270b9ac9191ab88da8fa8596672f9';
  final readaccesstoken =
      'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NDUyNzBiOWFjOTE5MWFiODhkYThmYTg1OTY2NzJmOSIsInN1YiI6IjYzZmUwMDAzOTY1M2Y2MDA4NTNjODI1NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.uoY53pRFa_wIfO4N6srilh244x9NBr8bFLTzuVh7Vgc';

  @override
  void initState() {
    loadmovies();
    super.initState();
  }

  loadmovies() async {
    TMDB tmdbWithCustomLogs = TMDB(ApiKeys(apikey, readaccesstoken),
        logConfig: ConfigLogger(showLogs: true, showErrorLogs: true));
    Map trendingresult = await tmdbWithCustomLogs.v3.trending.getTrending();
    Map topratedresult = await tmdbWithCustomLogs.v3.movies.getTopRated();
    Map tvresult = await tmdbWithCustomLogs.v3.tv.getTopRated();

    setState(() {
      trendingmovies = trendingresult['results'];
      topratedmovies = topratedresult['results'];
      tv = tvresult['results'];
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: ListView(
        children: [
          SizedBox(height: 25),
          TrendingMovies(trending: trendingmovies),
          TopRated(toprated: topratedmovies),
          TV(tv: tv),
        ],
      ),
    );
  }
}
