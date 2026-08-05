# MinSpeed

Defines the minimum speed of a task. If the task speed is lower than the preset value for a specified period of time, the task fails. The failure cause is [LOW\_SPEED]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-agent-interface MinSpeed--><!--Device-agent-interface MinSpeed-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## duration

```TypeScript
duration: int
```

Duration during which the task speed can be lower than the minimum speed, in seconds. If the task speed is lower than the preset value for a specified period of time, the task fails. If the value is set to **0**, there is no minimum speed limit.

**Type:** int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-MinSpeed-duration: int--><!--Device-MinSpeed-duration: int-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## speed

```TypeScript
speed: long
```

Minimum speed of a task, in byte/s. If the task speed is lower than this value for a specified period of time, the task fails. If the value is set to **0**, there is no minimum speed limit.

**Type:** long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-MinSpeed-speed: long--><!--Device-MinSpeed-speed: long-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

