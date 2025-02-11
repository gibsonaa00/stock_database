#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <cstddef>
#include <unordered_map>


// Define a node structure
struct Node {
    std::string key;
    Node* next;
};

// Function to create a new node
Node* createNode(std::string value) {
    Node* newNode = new Node();
    newNode->key = value;
    newNode->next = nullptr;
    return newNode;
}

// Define a node structure
struct valueNode {
    std::string key;
    std::unordered_map<std::string,std::string> hashMap;
};

// Function to create a new node
valueNode* createvaluNode(int value) {
    valueNode* newNode = new valueNode();
    newNode->key = value;
    return newNode;
}


class jHelper{
    public:

    static bool hasEnteredDict(std::string component){
        component = trim(component);
        return (component.compare(0,1,"{")==0);

    }

    static bool hasLeftDict(std::string component){
        component = trim(component);
        return (component.compare(0,1,"}")==0);

    }

    static bool hasEnteredList(std::string component){
        component = trim(component);
        return (component.compare(0,1,"[")==0);


    }

    static bool hasLeftList(std::string component){
        component = trim(component);
        return (component.compare(0,1,"]")==0); 

    }

    static std::string trim(std::string component){
        if (component.compare(0,1," ")==0){
            component.erase(component.begin(),component.begin()+component.find_first_not_of(" "));

        }
        return component;
    }

    static std::string eraseFirstChar(std::string component){
        component = trim(component);
        return component.erase(0,1);

    }

    // Called after trim and isList and isDict
    static std::string removeBrackets(std::string component){ 
        component = trim(component);
        return component.substr(0,component.length()-2);
    }

    static std::string eraseKey(std::string component){
        component = trim(component);
        return component.erase(0,component.find_first_of(":")+1);
    }

    


    static std::string extractKey(std::string component){
        component = trim(component);
        return component.substr(0,component.find_first_of(":"));
    }

    static std::string eraseElement(std::string component){
        component = trim(component);
        return component.erase(0,component.find_first_of(",")+1);
    }

    


    static std::string extractElement(std::string component){
        component = trim(component);
        return component.substr(0,component.find_first_of(","));
    }


    


};

class json{

    public:
        std::string rawJSON;
        std::string currentKey;
        jHelper hc;
        json(std::string rJSON){
            rawJSON = rJSON;
            process();

        }
        void process(void){
            if (!rawJSON.empty()){
                if (hc.hasEnteredDict(rawJSON)){
                    rawJSON = hc.eraseFirstChar(rawJSON); // remove {

                    currentKey = hc.extractKey(rawJSON); // extract the key
                    rawJSON = hc.eraseKey(rawJSON); // remove the key from raw json leaves just the object
                    process();



                }
                if (hc.hasEnteredList(rawJSON)){
                    rawJSON = hc.eraseFirstChar(rawJSON); // remove {
                    std::cout << "1== " << rawJSON<< std::endl;
                    std::string placeHolder = rawJSON;
                    while (!hc.hasLeftList(rawJSON)){

                        rawJSON = hc.extractElement(placeHolder);
                        placeHolder = hc.eraseElement(placeHolder);
                        process();
                    }
                    rawJSON = placeHolder;

                }


            }

            
        }

};

int main(void){

    std::string jsonInput;
    std::string line;

    std::ifstream jsonFile("settings.json");
    while (std::getline(jsonFile,line)){
        jsonInput += line;
    }
    json test = json(jsonInput);
    return 0;

}