#ifndef PROCESSOR_H
#define PROCESSOR_H

__declspec(dllexport) void clean_text(const char* input, char* output, int max_len);
__declspec(dllexport) int  word_count(const char* text);

#endif // PROCESSOR_H