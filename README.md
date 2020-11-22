# encodey
A simple python script to encode basic XSS payloads using single or double encoding.

# Installation
```
git clone https://github.com/DFC302/encodey.git
cd encodey.git
```
# Usage

## Basic usage
```
echo '"><script>alert(1)</script>' | python3 encodey.py
```

```
cat payloads.txt | python3 encodey.py
```

## Single encoding
```
echo '"><script>alert(1)</script>' | python3 encodey.py --single
```

## Double encoding
```
echo '"><script>alert(1)</script>' | python3 encodey.py --double
```
