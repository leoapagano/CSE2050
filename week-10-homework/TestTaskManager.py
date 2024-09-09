import random
import unittest
from TaskManager import Entry, TaskManager



class TestTaskManager(unittest.TestCase):
	"""Test cases for the TaskManager class."""
	def test_add_remove_preset(self):
		"""Tests that a queue can have predetermined (some duplicate) items added in random order,
		and that the first few will still be removed in the right order. Then, attempts to readd them,
		and ensures that the entire list is removed in the right order."""

		# Choose entries; we will be checking that the priorities for airportd and timed are updated
		# Yes, I know these are their PIDs, no, I don't care
		IntendedRemovalOrder = [
			Entry(1017, "WindowServer"),
			Entry(601, "timed"),
			Entry(586, "apfsd"),
			Entry(583, "coreaudiod"),
			Entry(519, "opendirectoryd"),
			Entry(501, "airportd"),
			Entry(491, "configd"),
			Entry(479, "logd"),
			Entry(1, "launchd"),
			Entry(0, "kernel_task")
		]
		EntriesToAdd = [
			Entry(0, "kernel_task"),
			Entry(1, "launchd"),
			Entry(479, "logd"),
			Entry(491, "configd"),
			Entry(519, "opendirectoryd"),
			Entry(522, "timed"),
			Entry(567, "airportd"),
			Entry(586, "apfsd"),
			Entry(583, "coreaudiod"),
			Entry(1017, "WindowServer")
		]
		EntriesToReadd = [
			Entry(501, "airportd"),
			Entry(519, "opendirectoryd"),
			Entry(583, "coreaudiod"),
			Entry(586, "apfsd"),
			Entry(601, "timed"),
			Entry(1017, "WindowServer")
		]
		random.shuffle(EntriesToAdd)
		EntriesToAdd.append(Entry(501, "airportd"))
		EntriesToAdd.append(Entry(601, "timed"))

		# Build a queue
		Queue = TaskManager()
		for curr_entry in EntriesToAdd: Queue.add_process(curr_entry)

		# Remove first 6 items
		# For each item, test length, and test that the right item was removed
		for i in range(6):
			# Test length
			self.assertEqual(10-i, len(Queue))
			# Test that right item was removed
			last_pid_removed = Queue.remove_process()
			self.assertEqual(last_pid_removed, IntendedRemovalOrder[i].process_id)

		# Readd these items in a random order
		random.shuffle(EntriesToReadd)
		for curr_entry in EntriesToReadd: Queue.add_process(curr_entry)

		# Empty out entire list
		# For each item, test length, and test that the right item was removed
		for i in range(10):
			# Test length
			self.assertEqual(10-i, len(Queue))
			# Test that right item was removed
			last_pid_removed = Queue.remove_process()
			self.assertEqual(last_pid_removed, IntendedRemovalOrder[i].process_id)

		# Final test - queue should be empty now
		self.assertEqual(len(Queue), 0)
		with self.assertRaises(IndexError):
			Queue.remove_process()



if __name__ == "__main__":
	unittest.main()