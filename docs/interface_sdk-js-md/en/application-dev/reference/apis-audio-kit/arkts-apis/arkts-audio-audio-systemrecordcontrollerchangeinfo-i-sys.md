# SystemRecordControllerChangeInfo (System API)

定义系统录像控制器状态改变时携带的信息。它包括启用状态、应用程序UID和预期的音频源类型。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-audio-interface SystemRecordControllerChangeInfo--><!--Device-audio-interface SystemRecordControllerChangeInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## enabled

```TypeScript
enabled: boolean
```

是否启用系统录像控制器面板。true表示启用面板，false表示禁用面板。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemRecordControllerChangeInfo-enabled: boolean--><!--Device-SystemRecordControllerChangeInfo-enabled: boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

## sourceType

```TypeScript
sourceType?: SourceType
```

启用录制控制器时由应用程序配置的预期音频源类型。用于匹配对应的录制场景和降噪模式。

**Type:** [SourceType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-sourcetype-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemRecordControllerChangeInfo-sourceType?: SourceType--><!--Device-SystemRecordControllerChangeInfo-sourceType?: SourceType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

## uid

```TypeScript
uid?: int
```

触发系统记录控制器状态更改的应用程序的UID。取值限定为整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemRecordControllerChangeInfo-uid?: int--><!--Device-SystemRecordControllerChangeInfo-uid?: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

