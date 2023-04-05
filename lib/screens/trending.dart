import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';

class TrendingMovies extends StatelessWidget {
  final List trending;

  const TrendingMovies({super.key, required this.trending});

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            'Top Trending',
            style: TextStyle(fontFamily: 'Georgia',fontSize: 20, color: Colors.white, fontWeight: FontWeight.bold),
          ),
          SizedBox(height: 10),
          Container(
            height: 270,
            child: ListView.builder(
                scrollDirection: Axis.horizontal,
                itemCount: trending.length,
                itemBuilder: (context, index) {
                  return InkWell(
                    child: Container(
                      width: 140,
                      child: Column(
                        children: [
                          Container(
                            height: 200,
                            decoration: BoxDecoration(
                                image: DecorationImage(
                                    image: NetworkImage(
                              'https://image.tmdb.org/t/p/w500' +
                                  trending[index]['poster_path'],
                            ))),
                          ),
                          //Container(
                          // child: Text(trending[index]['title'] != null
                          //  ? trending[index]['title']
                          //    : 'Loading'),
                          //)
                        ],
                      ),
                    ),
                  );
                }),
          )
        ],
      ),
    );
  }
}
