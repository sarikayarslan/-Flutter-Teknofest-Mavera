import 'package:firebase_database/firebase_database.dart';
import 'package:flutter/material.dart';
import 'user.dart';


void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  final refDataBase = FirebaseDatabase.instance.reference();
  var data;
  User user;
  String isMasked;
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: "Mavera",
      home: Scaffold(
          appBar: AppBar(
            centerTitle: true,
            title: Text("Mavera",
              style: TextStyle(
              fontSize: 30,
              fontWeight: FontWeight.bold,

            ),),
          ),
          body: Column(
            children: [Container(
              height: 200,
              width: 200,
              child:Image.asset('images/background1.jpeg'),
              alignment: Alignment.center,

            ),
              StreamBuilder(
              stream: refDataBase.onValue,
                builder: (context, snapshot) {
                  if (snapshot.hasData &&
                      !snapshot.hasError &&
                      snapshot.data.snapshot.value != null) {
                    data = snapshot.data.snapshot.value;

                     user = User(data["User"]["HES"],data["User"]["Temperature"],data["User"]["haveMask"]);
                    print(user.hES);
                    print(user.temperature);
                    print(user.haveMask);
                    if(user.haveMask){
                      isMasked ="Maske Tespit Edildi";
                    }
                    else{
                      isMasked ="Maske Tespit Edilemedi";
                    }
                    return Center(
                      child: Column(
                        children: [Card(


                        ),
                          Text(user.hES,
                          style: TextStyle(
                            fontSize: 30,
                            fontWeight: FontWeight.bold,

                          ),),
                          Text(user.temperature.toString(),
                            style: TextStyle(
                              fontSize: 30,
                              fontWeight: FontWeight.bold,

                            ),),
                          Text(isMasked.toString(),
                            style: TextStyle(
                              fontSize: 30,
                              fontWeight: FontWeight.bold,

                            ),),
                        ],
                      ),
                    );

                  } else {}
                  return Container();
                },
              ),
            ],
          )),
    );
  }
}
