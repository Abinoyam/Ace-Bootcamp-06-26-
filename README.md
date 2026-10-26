# Ace-Bootcamp-06-26-
import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(home: FormDemo()));

class FormDemo extends StatefulWidget {
  @override
  State<FormDemo> createState() => _FormDemoState();
}

class _FormDemoState extends State<FormDemo> {
  bool accept = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Input Form")),
      body: Column(
        children: [
          TextFormField(decoration: InputDecoration(labelText: "Username")),
          TextFormField(decoration: InputDecoration(labelText: "Email")),
          SwitchListTile(
            title: Text("Accept Terms"),
            value: accept,
            onChanged: (v) => setState(() => accept = v),
          ),
        ],
      ),
    );
  }
}


2)import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(home: FormDemo()));

class FormDemo extends StatelessWidget {
  final keyForm = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) => Scaffold(
    appBar: AppBar(title: Text("Form Validation")),
    body: Padding(
      padding: EdgeInsets.all(16),
      child: Form(
        key: keyForm,
        child: Column(children: [
          TextFormField(
            obscureText: true,
            decoration: InputDecoration(labelText: "Password"),
            validator: (v) =>
                v == null || v.length < 6 ? "Minimum 6 characters" : null,
          ),
          ElevatedButton(
            onPressed: () {
              if (keyForm.currentState!.validate()) {
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(content: Text("Processing Data")),
                );
              }
            },
            child: Text("Submit"),
          ),
        ]),
      ),
    ),
  );
}
