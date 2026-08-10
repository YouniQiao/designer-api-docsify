# @ohos.ai.intelligentVoice

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-unnamed-declare namespace intelligentVoice--><!--Device-unnamed-declare namespace intelligentVoice-End-->

**系统能力：** SystemCapability.AI.IntelligentVoice.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { intelligentVoice } from 'kits/@kit.BasicServicesKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [createEnrollIntelligentVoiceEngine](arkts-basicservices-intelligentvoice-createenrollintelligentvoiceengine-f-sys.md#createenrollintelligentvoiceengine) | Obtains an {@link EnrollIntelligentVoiceEngine} instance. This method uses an asynchronous callback to return the EnrollIntelligentVoiceEngine instance. |
| [createEnrollIntelligentVoiceEngine](arkts-basicservices-intelligentvoice-createenrollintelligentvoiceengine-f-sys.md#createenrollintelligentvoiceengine-1) | Obtains an {@link EnrollIntelligentVoiceEngine} instance. This method uses a promise to return the EnrollIntelligentVoiceEngine instance. |
| [createWakeupIntelligentVoiceEngine](arkts-basicservices-intelligentvoice-createwakeupintelligentvoiceengine-f-sys.md#createwakeupintelligentvoiceengine) | Obtains an {@link WakeupIntelligentVoiceEngine} instance. This method uses an asynchronous callback to return the WakeupIntelligentVoiceEngine instance. |
| [createWakeupIntelligentVoiceEngine](arkts-basicservices-intelligentvoice-createwakeupintelligentvoiceengine-f-sys.md#createwakeupintelligentvoiceengine-1) | Obtains an {@link WakeupIntelligentVoiceEngine} instance. This method uses a promise to return the WakeupIntelligentVoiceEngine instance. |
| [getIntelligentVoiceManager](arkts-basicservices-intelligentvoice-getintelligentvoicemanager-f-sys.md#getintelligentvoicemanager) | Obtains an {@link IntelligentVoiceManager} instance. |
| [getWakeupManager](arkts-basicservices-intelligentvoice-getwakeupmanager-f-sys.md#getwakeupmanager) | Obtains an {@link WakeupManager} instance. |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [EnrollCallbackInfo](arkts-basicservices-intelligentvoice-enrollcallbackinfo-i-sys.md) | Describes enroll callback information. |
| [EnrollEngineConfig](arkts-basicservices-intelligentvoice-enrollengineconfig-i-sys.md) | Describes enroll engine config. |
| [EnrollIntelligentVoiceEngine](arkts-basicservices-intelligentvoice-enrollintelligentvoiceengine-i-sys.md) | Implements enroll intelligent voice engine. |
| [EnrollIntelligentVoiceEngineDescriptor](arkts-basicservices-intelligentvoice-enrollintelligentvoiceenginedescriptor-i-sys.md) | Describes enroll intelligent voice engine. |
| [EvaluationResult](arkts-basicservices-intelligentvoice-evaluationresult-i-sys.md) | Describes evaluation result. |
| [IntelligentVoiceManager](arkts-basicservices-intelligentvoice-intelligentvoicemanager-i-sys.md) | Implements intelligent voice management. |
| [UploadFile](arkts-basicservices-intelligentvoice-uploadfile-i-sys.md) | Describes upload file information. |
| [WakeupHapInfo](arkts-basicservices-intelligentvoice-wakeuphapinfo-i-sys.md) | Describes wakeup hap information. |
| [WakeupIntelligentVoiceEngine](arkts-basicservices-intelligentvoice-wakeupintelligentvoiceengine-i-sys.md) | Implements wakeup intelligent voice engine. |
| [WakeupIntelligentVoiceEngineCallbackInfo](arkts-basicservices-intelligentvoice-wakeupintelligentvoiceenginecallbackinfo-i-sys.md) | Describes wakeup intelligent voice engine callback information. |
| [WakeupIntelligentVoiceEngineDescriptor](arkts-basicservices-intelligentvoice-wakeupintelligentvoiceenginedescriptor-i-sys.md) | Describes wakeup intelligent voice engine. |
| [WakeupManager](arkts-basicservices-intelligentvoice-wakeupmanager-i-sys.md) | Implements wakeup management. |
| [WakeupSourceFile](arkts-basicservices-intelligentvoice-wakeupsourcefile-i-sys.md) | Describes wakeup source file information. |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 | 说明 |
| --- | --- |
| [CapturerChannel](arkts-basicservices-intelligentvoice-capturerchannel-e-sys.md) | Enumerates capturer channel. |
| [EnrollResult](arkts-basicservices-intelligentvoice-enrollresult-e-sys.md) | Enumerates enroll result. |
| [EvaluationResultCode](arkts-basicservices-intelligentvoice-evaluationresultcode-e-sys.md) | Enumerates evaluation result code. |
| [IntelligentVoiceEngineType](arkts-basicservices-intelligentvoice-intelligentvoiceenginetype-e-sys.md) | Enumerates intelligent voice engine type. |
| [IntelligentVoiceErrorCode](arkts-basicservices-intelligentvoice-intelligentvoiceerrorcode-e-sys.md) | Enumerates intelligent voice error code. |
| [SensibilityType](arkts-basicservices-intelligentvoice-sensibilitytype-e-sys.md) | Enumerates sensibility type. |
| [ServiceChangeType](arkts-basicservices-intelligentvoice-servicechangetype-e-sys.md) | Enumerates service change type. |
| [UploadFileType](arkts-basicservices-intelligentvoice-uploadfiletype-e-sys.md) | Enumerates upload file type. |
| [WakeupIntelligentVoiceEventType](arkts-basicservices-intelligentvoice-wakeupintelligentvoiceeventtype-e-sys.md) | Enumerates wakeup intelligent voice event type. |
<!--DelEnd-->

