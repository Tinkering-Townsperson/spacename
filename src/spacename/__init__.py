###################
# IMPORTS & SETUP #
###################

from typing import List, Tuple
__version__ = "1.0.0"


class Namespace(object):
	def __init__(self, **kwargs) -> None:
		"""Initialize namespace object.

		Args:
			**kwargs (any, optional): Attributes to populate namespace with.
		"""

		self.fill_from_dict(kwargs)

	def fill_from_dict(self, dictionary: dict) -> None:
		"""Populate Namespace using dict.

		Args:
			dictionary (dict): Dict to populate namespace with.
		"""

		for key in dictionary:
			setattr(self, key, dictionary[key])

	def to_dict(self) -> dict:
		"""Return dict of self.

		Returns:
			dict: Dict of self
		"""
		return self.__dict__

	def __repr__(self) -> str:
		"""Return string representation of self.

		Returns:
			str: String representation of self.
		"""

		type_name = type(self).__name__
		arg_strings = []
		star_args = {}
		for arg in self._get_args():
			arg_strings.append(repr(arg))
		for name, value in self._get_kwargs():
			if name.isidentifier():
				arg_strings.append('%s=%r' % (name, value))
			else:
				star_args[name] = value
		if star_args:
			arg_strings.append('**%s' % repr(star_args))
		return '%s(%s)' % (type_name, ', '.join(arg_strings))

	def __eq__(self, other) -> bool:
		"""Check that self is equal to other.

		Args:
			other (Namespace): Object to check against

		Returns:
			bool: Is self equal to other?
		"""
		return vars(self) == vars(other) if isinstance(other, type(self)) else NotImplemented

	def __contains__(self, key) -> bool:
		"""Check if self contains given key.

		Args:
			key (str): Key to look for

		Returns:
			bool: Is key in self?
		"""
		return key in self.__dict__

	def __iter__(self):
		"""Return iterator of self.

		Returns:
			list_iterator: Iterator of self
		"""
		return iter(self._get_kwargs())

	def _get_kwargs(self) -> List[Tuple[str]]:
		"""Return keyword arguments of self in a list of tuples.

		Returns:
			List[Tuple[str]]: List of self's keyword arguments.
		"""
		return list(self.__dict__.items())

	def _get_args(self) -> list:
		"""Return arguments of self in  list.

		Returns:
			list: List of self's arguments
		"""
		return []
