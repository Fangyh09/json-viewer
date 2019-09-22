# jsonviewer
print meta json structure

## Install
```bash
python setup.py install
```

## Usage
```python
from jsonviewer import view_json

fname = "foo.json"
with open(fname) as f:
	data = json.load(f)
view_json(data)
```

## Demo
```
<type 'list'>len=1011
	<type 'dict'>len=7
		key=joints_vis
			<type 'list'>len=16
				data: 1
		key=scale
			data: 3.374796
		key=center
			<type 'list'>len=2
				data: 698
		key=joints
			<type 'list'>len=16
				<type 'list'>len=2
					data: 694
		key=image
			data: 4485.jpg
```


