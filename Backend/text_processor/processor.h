#ifndef PROCESSOR_H
#define PROCESSOR_H

#if defined(_WIN32)
    #define EXPORT __declspec(dllexport)
#else
    #define EXPORT __attribute__((visibility("default")))
#endif

EXPORT void clean_text(const char* input, char* output, int max_len);
EXPORT int  word_count(const char* text);

#endif