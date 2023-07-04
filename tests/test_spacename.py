from spacename import __version__, Namespace


def test_version():
	assert __version__ == "1.0.0"


def test_init():
	ns = Namespace(spam="foo", eggs="bar", bacon="baz")

	assert ns.spam == "foo"
	assert ns.eggs == "bar"
	assert ns.bacon == "baz"


def test_from_dict():
	dictionary = {
		"spam": "foo",
		"eggs": "bar",
		"bacon": "baz",
	}
	ns = Namespace()
	ns.fill_from_dict(dictionary)

	assert ns.spam == "foo"
	assert ns.eggs == "bar"
	assert ns.bacon == "baz"


def test_to_dict():
	ns = Namespace(spam="foo", eggs="bar", bacon="baz")
	dictionary = ns.to_dict()

	assert dictionary == {
		"spam": "foo",
		"eggs": "bar",
		"bacon": "baz",
	}


def test_repr():
	ns = Namespace(spam="foo", eggs="bar", bacon="baz")

	assert repr(ns) == "Namespace(spam='foo', eggs='bar', bacon='baz')"


def test_eq():
	ns1 = Namespace()
	ns2 = Namespace()

	assert ns1 == ns2


def test_contains():
	ns = Namespace(spam="foo", eggs="bar", bacon="baz")

	assert "spam" in ns
	assert "eggs" in ns
	assert "bacon" in ns


def test_iter():
	ns = Namespace(spam="foo", eggs="bar", bacon="baz")
	s = ""
	for key, value in iter(ns):
		s += f"{key}={value},\n"

	assert s == "spam=foo,\neggs=bar,\nbacon=baz,\n"


def test_get_kwargs():
	ns = Namespace(spam="foo", eggs="bar", bacon="baz")
	kwargs = ns._get_kwargs()

	assert kwargs == [("spam", "foo"), ("eggs", "bar"), ("bacon", "baz")]


def test_get_args():
	ns = Namespace()
	assert not ns._get_args()
