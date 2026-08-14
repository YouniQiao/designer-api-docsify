# event

Provides event name constants, including system event name constants and application event name constants. <br>The application event name constants are optional custom event names reserved when you call Write for application event logging.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-hiAppEvent-namespace event--><!--Device-hiAppEvent-namespace event-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## Modules to Import

```TypeScript
import { hiAppEvent } from 'hiAppEvent';
```

## Summary

### Constants

| Name | Description |
| --- | --- |
| [USER_LOGIN](arkts-performanceanalysis-event-con.md#USER_LOGIN) | User login event. This is a reserved application event name constant. **Atomic service API**: This parameter can be used in atomic services since API version 11. |
| [USER_LOGOUT](arkts-performanceanalysis-event-con.md#USER_LOGOUT) | User logout event. This is a reserved application event name constant. **Atomic service API**: This parameter can be used in atomic services since API version 11. |
| [DISTRIBUTED_SERVICE_START](arkts-performanceanalysis-event-con.md#DISTRIBUTED_SERVICE_START) | Distributed service startup event. This is a reserved application event name constant. **Atomic service API**: This parameter can be used in atomic services since API version 11. |
| [APP_CRASH](arkts-performanceanalysis-event-con.md#APP_CRASH) | Application crash event. This is a system event name constant. **Atomic service API**: This parameter can be used in atomic services since API version 11. |
| [APP_FREEZE](arkts-performanceanalysis-event-con.md#APP_FREEZE) | Application freeze event. This is a system event name constant. **Atomic service API**: This parameter can be used in atomic services since API version 11. |
| [APP_LAUNCH](arkts-performanceanalysis-event-con.md#APP_LAUNCH) | Event indicating the application launch duration. This is a system event name constant. **Atomic service API**: This parameter can be used in atomic services since API version 12. |
| [SCROLL_JANK](arkts-performanceanalysis-event-con.md#SCROLL_JANK) | Event indicating frame loss during swiping. This is a system event name constant. **Atomic service API**: This parameter can be used in atomic services since API version 12. |
| [CPU_USAGE_HIGH](arkts-performanceanalysis-event-con.md#CPU_USAGE_HIGH) | Event indicating a high CPU usage. This is a system event name constant. **Atomic service API**: This parameter can be used in atomic services since API version 12. |
| [BATTERY_USAGE](arkts-performanceanalysis-event-con.md#BATTERY_USAGE) | Event indicating battery usage statistics. This is a system event name constant. **Atomic service API**: This parameter can be used in atomic services since API version 12. |
| [RESOURCE_OVERLIMIT](arkts-performanceanalysis-event-con.md#RESOURCE_OVERLIMIT) | Application resource leak event. This is a system event name constant. **Atomic service API**: This parameter can be used in atomic services since API version 12. |
| [ADDRESS_SANITIZER](arkts-performanceanalysis-event-con.md#ADDRESS_SANITIZER) | Application address sanitizer event. This is a system event name constant. **Atomic service API**: This parameter can be used in atomic services since API version 12. |
| [MAIN_THREAD_JANK](arkts-performanceanalysis-event-con.md#MAIN_THREAD_JANK) | Main thread jank event. This is a system event name constant. **Atomic service API**: This parameter can be used in atomic services since API version 12. |
| [APP_KILLED](arkts-performanceanalysis-event-con.md#APP_KILLED) | Application killed event. This is a system event name constant. **Atomic service API**: This parameter can be used in atomic services since API version 20. |
| [APP_HICOLLIE](arkts-performanceanalysis-event-con.md#APP_HICOLLIE) | Application task execution timeout event. This is a system event name constant. **Atomic service API**: This parameter can be used in atomic services since API version 21. |
| [AUDIO_JANK_FRAME](arkts-performanceanalysis-event-con.md#AUDIO_JANK_FRAME) | Audio jank event. This is a system event name constant. **Atomic service API**: This parameter can be used in atomic services since API version 21. |
| [SCROLL_ARKWEB_FLING_JANK](arkts-performanceanalysis-event-con.md#SCROLL_ARKWEB_FLING_JANK) | ArkWeb fling jank event. This is a system event name constant. **Atomic service API**: This parameter can be used in atomic services since API version 23. |
| [appFreezeWarning](arkts-performanceanalysis-event-con.md#appFreezeWarning) | Application freeze warning event. This is a system event name constant. **Model restriction**: This API can be used only in the stage model. **Atomic service API**: This parameter can be used in atomic services since API version 26.0.0. |

