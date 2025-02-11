#include <stdio.h>
#include <string>
#include <curl/curl.h>
#include <fstream>


class request {
    public:
        std::string reqURLTemplate;
        std::string ticker;
        std::string host;
        std::string userAgent;
        std::string accept;
        std::string acceptLanguage;

        request(std::string rUT, std::string tick){
            reqURLTemplate = rUT;
            ticker = tick;

        }

};

int main(int argc, char **argv){




    CURL *curl;
    CURLcode res;
    struct curl_slist *headers = nullptr;
    //string url = argv[1];

    
    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();
    if(curl)  {

        curl_easy_setopt(curl, CURLOPT_URL,argv[1]);

        headers = curl_slist_append(headers, "Host: query1.finance.yahoo.com");
       

        // Set the headers
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

        // Performs reequest and stroed in res
        res = curl_easy_perform(curl);
        // Error handling
        if (res!= CURLE_OK){
            fprintf(stderr, "Request failed: %s\n", curl_easy_strerror(res));
        }
        curl_easy_cleanup(curl);
        curl_global_cleanup();

        
    }
    return 0;
}
