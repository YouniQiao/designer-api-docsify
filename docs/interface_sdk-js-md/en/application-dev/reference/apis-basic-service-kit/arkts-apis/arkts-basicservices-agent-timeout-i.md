# Timeout

Defines the timeout configuration of a task. The task waiting duration is not counted. For details about the waiting reasons, see  
[WaitingReason\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_20+\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-agent-interface Timeout--><!--Device-agent-interface Timeout-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## connectionTimeout

```TypeScript
connectionTimeout?: int
```

Task connection timeout interval, in seconds. The connection timeout interval indicates the maximum time required for establishing a connection between the client and server. If this parameter is not set, the default value **60** is used. The minimum value is **1**.

**Type:** int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Timeout-connectionTimeout?: int--><!--Device-Timeout-connectionTimeout?: int-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## totalTimeout

```TypeScript
totalTimeout?: int
```

Total timeout interval of a task, in seconds. The total timeout interval includes the time required for establishing a connection, sending a request, and receiving a response. If this parameter is not set, the default value **604800** is used. The minimum value is **1**, and the maximum value is **604800** (that is, one week).

**Type:** int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Timeout-totalTimeout?: int--><!--Device-Timeout-totalTimeout?: int-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

