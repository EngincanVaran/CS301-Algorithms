#include <iostream>
#include <string>
#include <vector>

using namespace std;

string lcs(vector<string>);
string lcsBack(vector<string> strings, vector<int> indexes, vector<string> cache);
int calcCachePos(vector<int> indexes, vector<string> strings);


string lcs(vector<string> strings)
{
	if (strings.size() == 0)
        return "";
    if (strings.size() == 1)
        return strings[0];
    int max = -1;
    int cacheSize = 1;
    for (int i = 0; i < strings.size(); i++)
    {
        cacheSize *= strings[i].size();
        if (strings[i].size() > max)
            max = strings[i].size();
    }
	vector<string> cache(cacheSize); // = new string[cacheSize];
	vector<int> indexes(strings.size()); //int[] indexes = new int[strings.Length];
    for (int i = 0; i < indexes.size(); i++)
        indexes[i] = strings[i].size() - 1;
    return lcsBack(strings, indexes, cache);
}
string lcsBack(vector<string> strings, vector<int> indexes, vector<string> cache)
{
    for (int i = 0; i < indexes.size(); i++ )
        if (indexes[i] == -1)
            return "";
    bool match = true;
    for (int i = 1; i < indexes.size(); i++)
    {
        if (strings[0][indexes[0]] != strings[i][indexes[i]])
        {
            match = false;
            break;
        }
    }
    if (match)
    {
		vector<int> newIndexes(indexes.size()); //int[] newIndexes = new int[indexes.Length];
        for (int i = 0; i < indexes.size(); i++)
            newIndexes[i] = indexes[i] - 1;
        string result = lcsBack(strings, newIndexes, cache) + strings[0][indexes[0]];
        cache[calcCachePos(indexes, strings)] = result;
        return result;
    }
    else
    {
		vector<string> subStrings(strings.size()); //string[] subStrings = new string[strings.Length];
        for (int i = 0; i < strings.size(); i++)
        {
            if (indexes[i] <= 0)
                subStrings[i] = "";
            else
            {
                vector<int> newIndexes(indexes.size());
                for (int j = 0; j < indexes.size(); j++)
                    newIndexes[j] = indexes[j];
                newIndexes[i]--;
                int cachePos = calcCachePos(newIndexes, strings);
				if (cache[cachePos] == "")		//care
                    subStrings[i] = lcsBack(strings, newIndexes, cache);
                else
                    subStrings[i] = cache[cachePos];
            }
        }
        string longestString = "";
        int longestLength = 0;
        for (int i = 0; i < subStrings.size(); i++)
        {
            if (subStrings[i].size() > longestLength)
            {
                longestString = subStrings[i];
                longestLength = longestString.size();
            }
        }
        cache[calcCachePos(indexes, strings)] = longestString;
        return longestString;
    }
}
int calcCachePos(vector<int> indexes, vector<string> strings)
{
    int factor = 1;
    int pos = 0;
    for (int i = 0; i < indexes.size(); i++)
    {
        pos += indexes[i] * factor;
		factor *= strings[i].size();
    }
    return pos;
}


int main()
{
	vector<string> temp;

	temp.push_back("666222054263314443712");
	temp.push_back("5432127413542377777");
	temp.push_back("6664664565464057425");

	cout << lcs(temp);



	return 0;
}