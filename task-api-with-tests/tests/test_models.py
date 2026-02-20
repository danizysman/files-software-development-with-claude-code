"""Tests for models.py.

NOTE: models.py does not currently have a TaskStore class, get_by_user, or
delete. It exposes module-level functions over a shared in-memory list.
Tests below cover the existing public API.  get_by_user and delete would
require additions to models.py before they can be tested.
"""
import pytest
import models


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(autouse=True)
def reset_store():
    """Reset the in-memory store before every test."""
    models._tasks.clear()
    models._next_id = 1
    yield


# ---------------------------------------------------------------------------
# create_task
# ---------------------------------------------------------------------------

class TestCreateTask:
    def test_creates_task_with_title(self):
        task = models.create_task("Buy milk")
        assert task.title == "Buy milk"

    def test_creates_task_with_description(self):
        task = models.create_task("Buy milk", description="2% fat")
        assert task.description == "2% fat"

    def test_description_defaults_to_empty_string(self):
        task = models.create_task("No desc")
        assert task.description == ""

    def test_assigns_sequential_ids(self):
        first = models.create_task("First")
        second = models.create_task("Second")
        assert first.id == 1
        assert second.id == 2

    def test_completed_defaults_to_false(self):
        task = models.create_task("New task")
        assert task.completed is False

    def test_created_at_is_set(self):
        task = models.create_task("New task")
        assert task.created_at is not None

    def test_task_is_persisted_in_store(self):
        task = models.create_task("Stored task")
        assert task in models._tasks

    # Edge cases
    def test_empty_title_is_accepted(self):
        # models.py applies no validation; an empty title creates a task.
        # If validation is added later this test should be updated.
        task = models.create_task("")
        assert task.title == ""
        assert task in models._tasks

    def test_whitespace_only_title_is_accepted(self):
        task = models.create_task("   ")
        assert task.title == "   "

    def test_multiple_tasks_with_same_title_get_different_ids(self):
        t1 = models.create_task("Duplicate")
        t2 = models.create_task("Duplicate")
        assert t1.id != t2.id


# ---------------------------------------------------------------------------
# get_all_tasks
# ---------------------------------------------------------------------------

class TestGetAllTasks:
    def test_returns_empty_list_when_no_tasks(self):
        assert models.get_all_tasks() == []

    def test_returns_all_created_tasks(self):
        models.create_task("A")
        models.create_task("B")
        tasks = models.get_all_tasks()
        assert len(tasks) == 2

    def test_returns_tasks_in_insertion_order(self):
        models.create_task("First")
        models.create_task("Second")
        titles = [t.title for t in models.get_all_tasks()]
        assert titles == ["First", "Second"]


# ---------------------------------------------------------------------------
# get_task_by_id
# ---------------------------------------------------------------------------

class TestGetTaskById:
    def test_returns_task_when_found(self):
        task = models.create_task("Find me")
        result = models.get_task_by_id(task.id)
        assert result is task

    def test_returns_none_when_not_found(self):
        assert models.get_task_by_id(999) is None

    def test_returns_none_on_empty_store(self):
        assert models.get_task_by_id(1) is None

    def test_returns_correct_task_among_many(self):
        models.create_task("A")
        target = models.create_task("Target")
        models.create_task("C")
        result = models.get_task_by_id(target.id)
        assert result.title == "Target"


# ---------------------------------------------------------------------------
# Task.to_dict
# ---------------------------------------------------------------------------

class TestTaskToDict:
    def test_to_dict_contains_expected_keys(self):
        task = models.create_task("Dict task", description="desc")
        d = task.to_dict()
        assert set(d.keys()) == {"id", "title", "description", "created_at", "completed"}

    def test_to_dict_values_match_task(self):
        task = models.create_task("Dict task", description="desc")
        d = task.to_dict()
        assert d["id"] == task.id
        assert d["title"] == "Dict task"
        assert d["description"] == "desc"
        assert d["completed"] is False

    def test_to_dict_created_at_is_iso_string(self):
        task = models.create_task("ISO task")
        d = task.to_dict()
        # Should not raise
        from datetime import datetime
        datetime.fromisoformat(d["created_at"])


      
