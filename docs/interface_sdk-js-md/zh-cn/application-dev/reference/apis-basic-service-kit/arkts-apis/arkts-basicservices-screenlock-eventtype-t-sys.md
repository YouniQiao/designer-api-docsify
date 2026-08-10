# EventType（系统接口）

```TypeScript
type EventType =
    'beginWakeUp'
    | 'endWakeUp'
    | 'beginScreenOn'
    | 'endScreenOn'
    | 'beginScreenOff'
    | 'endScreenOff'
    | 'unlockScreen'
    | 'lockScreen'
    | 'beginExitAnimation'
    | 'beginSleep'
    | 'endSleep'
    | 'changeUser'
    | 'screenlockEnabled'
    | 'serviceRestart'
    | 'strongAuthChanged'
    | 'screenLockDisabledChanged'
    | 'unlockPolicyChanged'
```

Indicates the system event type related to the screen lock management service. Added unlockPolicyChanged.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-screenLock-type EventType =    'beginWakeUp'    | 'endWakeUp'    | 'beginScreenOn'    | 'endScreenOn'    | 'beginScreenOff'    | 'endScreenOff'    | 'unlockScreen'    | 'lockScreen'    | 'beginExitAnimation'    | 'beginSleep'    | 'endSleep'    | 'changeUser'    | 'screenlockEnabled'    | 'serviceRestart'    | 'strongAuthChanged'    | 'screenLockDisabledChanged'    | 'unlockPolicyChanged'--><!--Device-screenLock-type EventType =    'beginWakeUp'    | 'endWakeUp'    | 'beginScreenOn'    | 'endScreenOn'    | 'beginScreenOff'    | 'endScreenOff'    | 'unlockScreen'    | 'lockScreen'    | 'beginExitAnimation'    | 'beginSleep'    | 'endSleep'    | 'changeUser'    | 'screenlockEnabled'    | 'serviceRestart'    | 'strongAuthChanged'    | 'screenLockDisabledChanged'    | 'unlockPolicyChanged'-End-->

**系统能力：** SystemCapability.MiscServices.ScreenLock

**系统接口：** 此接口为系统接口。

| 类型 | 说明 |
| --- | --- |
| 'beginWakeUp' |  |
| 'endWakeUp' |  |
| 'beginScreenOn' |  |
| 'endScreenOn' |  |
| 'beginScreenOff' |  |
| 'endScreenOff' |  |
| 'unlockScreen' |  |
| 'lockScreen' |  |
| 'beginExitAnimation' |  |
| 'beginSleep' |  |
| 'endSleep' |  |
| 'changeUser' |  |
| 'screenlockEnabled' |  |
| 'serviceRestart' |  |
| 'strongAuthChanged' |  |
| 'screenLockDisabledChanged' |  |
| 'unlockPolicyChanged' |  |

