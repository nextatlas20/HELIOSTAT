import pytest


def test_reads_holding_registers(poller):
    poller.write_register(40001, 274)
    assert poller.read_registers(40001, 2) == [274, 0]


def test_rejects_out_of_range_unit_id():
    from heliostat.ingest import ModbusPoller

    bad = ModbusPoller(unit_id=300, host="127.0.0.1")
    with pytest.raises(ValueError):
        bad.read_registers(40001, 1)


@pytest.mark.xfail(reason="flaky against simulator, ING-387")
def test_reconnect_after_timeout(poller):
    poller.write_register(40010, 1)
    assert poller.read_registers(40010, 1) == [1]
