# SystemSoundManager

管理系统声音。在调用SystemSoundManager的接口前，需要先通过[getSystemSoundManager](arkts-audio-systemsoundmanager-getsystemsoundmanager-f.md#getSystemSoundManager)创建实例。

**起始版本：** 10

<!--Device-systemSoundManager-interface SystemSoundManager--><!--Device-systemSoundManager-interface SystemSoundManager-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

## addCustomizedTone

```TypeScript
addCustomizedTone(context: BaseContext, toneAttr: ToneAttrs, externalUri: string): Promise<string>
```

通过铃音uri将自定义铃音添加到铃音库。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.WRITE_RINGTONE

<!--Device-SystemSoundManager-addCustomizedTone(context: BaseContext, toneAttr: ToneAttrs, externalUri: string): Promise<string>--><!--Device-SystemSoundManager-addCustomizedTone(context: BaseContext, toneAttr: ToneAttrs, externalUri: string): Promise<string>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| toneAttr | [ToneAttrs](arkts-audio-systemsoundmanager-toneattrs-i.md) | 是 |
| externalUri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [20700006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio-ringtone-sys.md#20700006-rom空间不足) |
| [20700005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio-ringtone-sys.md#20700005-文件个数超过限制) |
| [20700004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio-ringtone-sys.md#20700004-数据大小超过限制) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let title = 'test'; // 需更改为实际名称。
let fileName = 'displayName_test'; // 需更改为实际文件名。
let categoryValue = systemSoundManager.TONE_CATEGORY_ALARM;

let toneAttrs = systemSoundManager.createCustomizedToneAttrs();
toneAttrs.setTitle(title);
toneAttrs.setFileName(fileName);
toneAttrs.setCategory(categoryValue);

let path = 'file://data/test.ogg'; // 需更改为实际铃音uri。

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.addCustomizedTone(context, toneAttrs, path).then((value: string) => {
  console.info('Succeeded in doing addCustomizedTone.');
}).catch((err: BusinessError) => {
  console.error(`Failed to addCustomizedTone. Code: ${err.code}, message: ${err.message}`);
});
```

## addCustomizedTone

```TypeScript
addCustomizedTone(context: BaseContext, toneAttr: ToneAttrs, fd: number, offset?: number, length?: number)
      : Promise<string>
```

通过文件描述符fd将自定义铃音添加到铃音库。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.WRITE_RINGTONE

<!--Device-SystemSoundManager-addCustomizedTone(context: BaseContext, toneAttr: ToneAttrs, fd: int, offset?: long, length?: long)      : Promise<string>--><!--Device-SystemSoundManager-addCustomizedTone(context: BaseContext, toneAttr: ToneAttrs, fd: int, offset?: long, length?: long)      : Promise<string>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| toneAttr | [ToneAttrs](arkts-audio-systemsoundmanager-toneattrs-i.md) | 是 |
| fd | number | 是 |
| offset | number | 否 |
| length | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [20700006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio-ringtone-sys.md#20700006-rom空间不足) |
| [20700005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio-ringtone-sys.md#20700005-文件个数超过限制) |
| [20700004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio-ringtone-sys.md#20700004-数据大小超过限制) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let title = 'test'; // 需更改为实际名称。
let fileName = 'displayName_test'; // 需更改为实际文件名。
let categoryValue = systemSoundManager.TONE_CATEGORY_ALARM;

let toneAttrs = systemSoundManager.createCustomizedToneAttrs();
toneAttrs.setTitle(title);
toneAttrs.setFileName(fileName);
toneAttrs.setCategory(categoryValue);

let fd = 10; // 需更改为实际铃音fd。
let offset = 0; // 需更改为实际所需偏移量。
let length = 50; // 需更改为实际所需数据长度。

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.addCustomizedTone(context, toneAttrs, fd, offset, length).then((value: string) => {
  console.info('Succeeded in doing addCustomizedTone.');
}).catch((err: BusinessError) => {
  console.error(`Failed to addCustomizedTone. Code: ${err.code}, message: ${err.message}`);
});
```

## close

```TypeScript
close(fd: number): Promise<void>
```

关闭闹铃文件。使用Promise异步回调。

**起始版本：** 12

<!--Device-SystemSoundManager-close(fd: int): Promise<void>--><!--Device-SystemSoundManager-close(fd: int): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let fd = 50; // 需更改为目标铃声的fd。

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.close(fd).then(() => {
  console.info('Succeeded in doing close.');
}).catch((err: BusinessError) => {
  console.error(`Failed to close. Code: ${err.code}, message: ${err.message}`);
});
```

## getAlarmToneAttrList

```TypeScript
getAlarmToneAttrList(context: BaseContext): Promise<ToneAttrsArray>
```

获取全部闹铃属性列表。使用Promise异步回调。

**起始版本：** 12

<!--Device-SystemSoundManager-getAlarmToneAttrList(context: BaseContext): Promise<ToneAttrsArray>--><!--Device-SystemSoundManager-getAlarmToneAttrList(context: BaseContext): Promise<ToneAttrsArray>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ToneAttrsArray](arkts-audio-systemsoundmanager-toneattrsarray-t.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getAlarmToneAttrList(context).then((value: systemSoundManager.ToneAttrsArray) => {
  console.info('Succeeded in doing getAlarmToneAttrList.');
}).catch((err: BusinessError) => {
  console.error(`Failed to getAlarmToneAttrList. Code: ${err.code}, message: ${err.message}`);
});
```

## getAlarmToneUri

```TypeScript
getAlarmToneUri(context: BaseContext): Promise<string>
```

获取系统当前闹铃uri。使用Promise异步回调。

**起始版本：** 12

<!--Device-SystemSoundManager-getAlarmToneUri(context: BaseContext): Promise<string>--><!--Device-SystemSoundManager-getAlarmToneUri(context: BaseContext): Promise<string>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getAlarmToneUri(context).then((value: string) => {
  console.info('Succeeded in doing getAlarmToneUri.');
}).catch((err: BusinessError) => {
  console.error(`Failed to getAlarmToneUri. Code: ${err.code}, message: ${err.message}`);
});
```

## getCurrentRingtoneAttribute

```TypeScript
getCurrentRingtoneAttribute(type: RingtoneType): Promise<ToneAttrs>
```

获取正在使用的铃声属性。使用Promise异步回调。

**起始版本：** 20

<!--Device-SystemSoundManager-getCurrentRingtoneAttribute(type: RingtoneType): Promise<ToneAttrs>--><!--Device-SystemSoundManager-getCurrentRingtoneAttribute(type: RingtoneType): Promise<ToneAttrs>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ToneAttrs](arkts-audio-systemsoundmanager-toneattrs-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let type: systemSoundManager.RingtoneType = systemSoundManager.RingtoneType.RINGTONE_TYPE_SIM_CARD_0;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getCurrentRingtoneAttribute(type).then((value: systemSoundManager.ToneAttrs) => {
  console.info('Succeeded in doing getCurrentRingtoneAttribute.');
}).catch((err: BusinessError) => {
  console.error(`Failed to getCurrentRingtoneAttribute. Code: ${err.code}, message: ${err.message}`);
});
```

## getDefaultAlarmToneAttrs

```TypeScript
getDefaultAlarmToneAttrs(context: BaseContext): Promise<ToneAttrs>
```

获取系统闹铃的属性。使用Promise异步回调。

**起始版本：** 12

<!--Device-SystemSoundManager-getDefaultAlarmToneAttrs(context: BaseContext): Promise<ToneAttrs>--><!--Device-SystemSoundManager-getDefaultAlarmToneAttrs(context: BaseContext): Promise<ToneAttrs>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ToneAttrs](arkts-audio-systemsoundmanager-toneattrs-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getDefaultAlarmToneAttrs(context).then((value: systemSoundManager.ToneAttrs) => {
  console.info('Succeeded in doing getDefaultAlarmToneAttrs.');
}).catch((err: BusinessError) => {
  console.error(`Failed to getDefaultAlarmToneAttrs. Code: ${err.code}, message: ${err.message}`);
});
```

## getDefaultRingtoneAttrs

```TypeScript
getDefaultRingtoneAttrs(context: BaseContext, type: RingtoneType): Promise<ToneAttrs>
```

获取系统铃声的属性。使用Promise异步回调。

**起始版本：** 12

<!--Device-SystemSoundManager-getDefaultRingtoneAttrs(context: BaseContext, type: RingtoneType): Promise<ToneAttrs>--><!--Device-SystemSoundManager-getDefaultRingtoneAttrs(context: BaseContext, type: RingtoneType): Promise<ToneAttrs>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ToneAttrs](arkts-audio-systemsoundmanager-toneattrs-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let type: systemSoundManager.RingtoneType = systemSoundManager.RingtoneType.RINGTONE_TYPE_SIM_CARD_0;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getDefaultRingtoneAttrs(context, type).then((value: systemSoundManager.ToneAttrs) => {
  console.info('Succeeded in doing getDefaultRingtoneAttrs.');
}).catch((err: BusinessError) => {
  console.error(`Failed to getDefaultRingtoneAttrs. Code: ${err.code}, message: ${err.message}`);
});
```

## getDefaultSystemToneAttrs

```TypeScript
getDefaultSystemToneAttrs(context: BaseContext, type: SystemToneType): Promise<ToneAttrs>
```

获取系统提示音的属性。使用Promise异步回调。

**起始版本：** 12

<!--Device-SystemSoundManager-getDefaultSystemToneAttrs(context: BaseContext, type: SystemToneType): Promise<ToneAttrs>--><!--Device-SystemSoundManager-getDefaultSystemToneAttrs(context: BaseContext, type: SystemToneType): Promise<ToneAttrs>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [SystemToneType](arkts-audio-systemsoundmanager-systemtonetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ToneAttrs](arkts-audio-systemsoundmanager-toneattrs-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let type: systemSoundManager.SystemToneType = systemSoundManager.SystemToneType.SYSTEM_TONE_TYPE_SIM_CARD_0;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getDefaultSystemToneAttrs(context, type).then((value: systemSoundManager.ToneAttrs) => {
  console.info('Succeeded in doing getDefaultSystemToneAttrs.');
}).catch((err: BusinessError) => {
  console.error(`Failed to getDefaultSystemToneAttrs. Code: ${err.code}, message: ${err.message}`);
});
```

## getHapticsAttrsSyncedWithTone

```TypeScript
getHapticsAttrsSyncedWithTone(context: BaseContext, toneUri: string): Promise<ToneHapticsAttrs>
```

获取与指定铃音同步的振动属性。使用Promise异步回调。

**起始版本：** 14

<!--Device-SystemSoundManager-getHapticsAttrsSyncedWithTone(context: BaseContext, toneUri: string): Promise<ToneHapticsAttrs>--><!--Device-SystemSoundManager-getHapticsAttrsSyncedWithTone(context: BaseContext, toneUri: string): Promise<ToneHapticsAttrs>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| toneUri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ToneHapticsAttrs](arkts-audio-systemsoundmanager-tonehapticsattrs-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [20700003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio-ringtone-sys.md#20700003-操作不支持) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let toneUri: string = '/data/storage/el2/base/RingTone/alarms/test.ogg'; // 需更改为实际铃音uri。

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getHapticsAttrsSyncedWithTone(context, toneUri).then((value: systemSoundManager.ToneHapticsAttrs) => {
  console.info('Succeeded in doing getHapticsAttrsSyncedWithTone.');
}).catch((err: BusinessError) => {
  console.error(`Failed to getHapticsAttrsSyncedWithTone. Code: ${err.code}, message: ${err.message}`);
});
```

## getMockHapticRingtonePlayer

```TypeScript
getMockHapticRingtonePlayer(
      context: BaseContext, type: RingtoneType, ringtoneUri: string): Promise<RingtonePlayer | null>
```

获取模拟触觉铃声播放器，根据指定的铃声类型和铃音文件URI，播放该铃音文件对应的振动文件及其模拟触觉声音文件。使用Promise异步回调。

> **说明：**
> 
> - 调用该接口前，请确保传入的ringtoneUri在系统中存在，否则会出现异常和错误。例如无法播放匹配的触觉声音文件。
> 
> - 通过该接口获取实例后，在服务终止时需主动调用RingtonePlayer的
> [release](arkts-audio-ringtoneplayer-ringtoneplayer-i-sys.md#release)方法释放播放器资源。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SystemSoundManager-getMockHapticRingtonePlayer(      context: BaseContext, type: RingtoneType, ringtoneUri: string): Promise<RingtonePlayer | null>--><!--Device-SystemSoundManager-getMockHapticRingtonePlayer(      context: BaseContext, type: RingtoneType, ringtoneUri: string): Promise<RingtonePlayer | null>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | 是 |
| [ringtoneUri](../../apis-notification-kit/arkts-apis/arkts-notification-notificationmanager-ringtoneinfo-i-sys.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;RingtonePlayer \ | null & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [20700002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio-ringtone-sys.md#20700002-参数检查失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let type: systemSoundManager.RingtoneType = systemSoundManager.RingtoneType.RINGTONE_TYPE_SIM_CARD_0;
let systemRingtonePlayer: systemSoundManager.RingtonePlayer | null = null;
let ringtoneUri = 'file://data/test.json'; // 需更改为目标铃音文件URI。

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getMockHapticRingtonePlayer(context, type, ringtoneUri).then((value: systemSoundManager.RingtonePlayer | null) => {
  if (value != null) {
    console.info('Succeeded in doing getMockHapticRingtonePlayer.');
    systemRingtonePlayer = value;
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to getMockHapticRingtonePlayer. Code: ${err.code}, message: ${err.message}`);
});
```

## getMockHapticRingtonePlayer

```TypeScript
getMockHapticRingtonePlayer(context: BaseContext, hapticUri: string): Promise<RingtonePlayer | null>
```

获取模拟触觉铃声播放器，根据指定的触觉文件URI播放振动文件及其对应的模拟触觉声音文件。使用Promise异步回调。

> **说明：**
> 
> - 调用该接口前，请确保传入的hapticUri在系统中存在，否则会出现异常和错误。例如无法播放匹配的触觉声音文件。
> 
> - 通过该接口获取实例后，在服务终止时需主动调用RingtonePlayer的
> [release](arkts-audio-ringtoneplayer-ringtoneplayer-i-sys.md#release)方法释放播放器资源。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SystemSoundManager-getMockHapticRingtonePlayer(context: BaseContext, hapticUri: string): Promise<RingtonePlayer | null>--><!--Device-SystemSoundManager-getMockHapticRingtonePlayer(context: BaseContext, hapticUri: string): Promise<RingtonePlayer | null>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| hapticUri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;RingtonePlayer \ | null & gt; |

**错误码：**

| 错误码ID |
| --- |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [20700002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio-ringtone-sys.md#20700002-参数检查失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let systemRingtonePlayer: systemSoundManager.RingtonePlayer | null = null;
let hapticUri = 'file://data/test.json'; // 需更改为目标触觉文件URI。

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getMockHapticRingtonePlayer(context, hapticUri).then((value: systemSoundManager.RingtonePlayer | null) => {
  if (value != null) {
    console.info('Succeeded in doing getMockHapticRingtonePlayer.');
    systemRingtonePlayer = value;
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to getMockHapticRingtonePlayer. Code: ${err.code}, message: ${err.message}`);
});
```

## getRingtoneAttrList

```TypeScript
getRingtoneAttrList(context: BaseContext, type: RingtoneType): Promise<ToneAttrsArray>
```

获取系统铃声的属性列表。使用Promise异步回调。

**起始版本：** 12

<!--Device-SystemSoundManager-getRingtoneAttrList(context: BaseContext, type: RingtoneType): Promise<ToneAttrsArray>--><!--Device-SystemSoundManager-getRingtoneAttrList(context: BaseContext, type: RingtoneType): Promise<ToneAttrsArray>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ToneAttrsArray](arkts-audio-systemsoundmanager-toneattrsarray-t.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let type: systemSoundManager.RingtoneType = systemSoundManager.RingtoneType.RINGTONE_TYPE_SIM_CARD_0;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getRingtoneAttrList(context, type).then((value: systemSoundManager.ToneAttrsArray) => {
  console.info('Succeeded in doing getRingtoneAttrList.');
}).catch((err: BusinessError) => {
  console.error(`Failed to getRingtoneAttrList. Code: ${err.code}, message: ${err.message}`);
});
```

## getRingtonePlayer

```TypeScript
getRingtonePlayer(context: BaseContext, type: RingtoneType): Promise<RingtonePlayer>
```

获取系统铃声播放器。使用Promise异步回调。

**起始版本：** 11

<!--Device-SystemSoundManager-getRingtonePlayer(context: BaseContext, type: RingtoneType): Promise<RingtonePlayer>--><!--Device-SystemSoundManager-getRingtonePlayer(context: BaseContext, type: RingtoneType): Promise<RingtonePlayer>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;RingtonePlayer & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let type: systemSoundManager.RingtoneType = systemSoundManager.RingtoneType.RINGTONE_TYPE_SIM_CARD_0;
let systemRingtonePlayer: systemSoundManager.RingtonePlayer | undefined = undefined;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getRingtonePlayer(context, type).then((value: systemSoundManager.RingtonePlayer) => {
  console.info('Succeeded in doing getRingtonePlayer.');
  systemRingtonePlayer = value;
}).catch((err: BusinessError) => {
  console.error(`Failed to getRingtonePlayer. Code: ${err.code}, message: ${err.message}`);
});
```

## getRingtoneUri

```TypeScript
getRingtoneUri(context: BaseContext, type: RingtoneType): Promise<string>
```

获取系统铃声uri。使用Promise异步回调。

**起始版本：** 11

<!--Device-SystemSoundManager-getRingtoneUri(context: BaseContext, type: RingtoneType): Promise<string>--><!--Device-SystemSoundManager-getRingtoneUri(context: BaseContext, type: RingtoneType): Promise<string>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let type: systemSoundManager.RingtoneType = systemSoundManager.RingtoneType.RINGTONE_TYPE_SIM_CARD_0;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getRingtoneUri(context, type).then((value: string) => {
  console.info('Succeeded in doing getRingtoneUri.');
}).catch((err: BusinessError) => {
  console.error(`Failed to getRingtoneUri. Code: ${err.code}, message: ${err.message}`);
});
```

## getSystemRingtonePlayer

```TypeScript
getSystemRingtonePlayer(context: Context, type: RingtoneType, callback: AsyncCallback<RingtonePlayer>): void
```

获取系统铃声播放器。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getRingtonePlayer](#getRingtonePlayer)

<!--Device-SystemSoundManager-getSystemRingtonePlayer(context: Context, type: RingtoneType, callback: AsyncCallback<RingtonePlayer>): void--><!--Device-SystemSoundManager-getSystemRingtonePlayer(context: Context, type: RingtoneType, callback: AsyncCallback<RingtonePlayer>): void-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;RingtonePlayer&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let type: systemSoundManager.RingtoneType = systemSoundManager.RingtoneType.RINGTONE_TYPE_DEFAULT;
let systemRingtonePlayer: systemSoundManager.RingtonePlayer | undefined = undefined;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getSystemRingtonePlayer(context, type, (err: BusinessError, value: systemSoundManager.RingtonePlayer) => {
  if (err) {
    console.error(`Failed to get system ringtone player. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate the value of the system ringtone player is obtained.`);
  systemRingtonePlayer = value;
});
```

## getSystemRingtonePlayer

```TypeScript
getSystemRingtonePlayer(context: Context, type: RingtoneType): Promise<RingtonePlayer>
```

获取系统铃声播放器。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getRingtonePlayer](#getRingtonePlayer)

<!--Device-SystemSoundManager-getSystemRingtonePlayer(context: Context, type: RingtoneType): Promise<RingtonePlayer>--><!--Device-SystemSoundManager-getSystemRingtonePlayer(context: Context, type: RingtoneType): Promise<RingtonePlayer>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;RingtonePlayer & gt; |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let type: systemSoundManager.RingtoneType = systemSoundManager.RingtoneType.RINGTONE_TYPE_DEFAULT;
let systemRingtonePlayer: systemSoundManager.RingtonePlayer | undefined = undefined;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getSystemRingtonePlayer(context, type).then((value: systemSoundManager.RingtonePlayer) => {
  console.info('Succeeded in doing getSystemRingtonePlayer.');
  systemRingtonePlayer = value;
}).catch((err: BusinessError) => {
  console.error(`Failed to getSystemRingtonePlayer. Code: ${err.code}, message: ${err.message}`);
});
```

## getSystemRingtoneUri

```TypeScript
getSystemRingtoneUri(context: Context, type: RingtoneType, callback: AsyncCallback<string>): void
```

获取系统铃声uri。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getRingtoneUri](#getRingtoneUri)

<!--Device-SystemSoundManager-getSystemRingtoneUri(context: Context, type: RingtoneType, callback: AsyncCallback<string>): void--><!--Device-SystemSoundManager-getSystemRingtoneUri(context: Context, type: RingtoneType, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let type: systemSoundManager.RingtoneType = systemSoundManager.RingtoneType.RINGTONE_TYPE_DEFAULT;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getSystemRingtoneUri(context, type, (err: BusinessError, value: string) => {
  if (err) {
    console.error(`Failed to get system ringtone uri. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate the value of the system ringtone uri is obtained ${value}.`);
});
```

## getSystemRingtoneUri

```TypeScript
getSystemRingtoneUri(context: Context, type: RingtoneType): Promise<string>
```

获取系统铃声uri。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getRingtoneUri](#getRingtoneUri)

<!--Device-SystemSoundManager-getSystemRingtoneUri(context: Context, type: RingtoneType): Promise<string>--><!--Device-SystemSoundManager-getSystemRingtoneUri(context: Context, type: RingtoneType): Promise<string>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let type: systemSoundManager.RingtoneType = systemSoundManager.RingtoneType.RINGTONE_TYPE_DEFAULT;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getSystemRingtoneUri(context, type).then((value: string) => {
  console.info('Succeeded in doing getSystemRingtoneUri.');
}).catch((err: BusinessError) => {
  console.error(`Failed to getSystemRingtoneUri. Code: ${err.code}, message: ${err.message}`);
});
```

## getSystemToneAttrList

```TypeScript
getSystemToneAttrList(context: BaseContext, type: SystemToneType): Promise<ToneAttrsArray>
```

获取系统提示音的属性列表。使用Promise异步回调。

**起始版本：** 12

<!--Device-SystemSoundManager-getSystemToneAttrList(context: BaseContext, type: SystemToneType): Promise<ToneAttrsArray>--><!--Device-SystemSoundManager-getSystemToneAttrList(context: BaseContext, type: SystemToneType): Promise<ToneAttrsArray>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [SystemToneType](arkts-audio-systemsoundmanager-systemtonetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ToneAttrsArray](arkts-audio-systemsoundmanager-toneattrsarray-t.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let type: systemSoundManager.SystemToneType = systemSoundManager.SystemToneType.SYSTEM_TONE_TYPE_SIM_CARD_0;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getSystemToneAttrList(context, type).then((value: systemSoundManager.ToneAttrsArray) => {
  console.info('Succeeded in doing getSystemToneAttrList.');
}).catch((err: BusinessError) => {
  console.error(`Failed to getSystemToneAttrList. Code: ${err.code}, message: ${err.message}`);
});
```

## getSystemTonePlayer

```TypeScript
getSystemTonePlayer(context: BaseContext, type: SystemToneType): Promise<SystemTonePlayer>
```

获取系统提示音播放器。使用Promise异步回调。

**起始版本：** 11

<!--Device-SystemSoundManager-getSystemTonePlayer(context: BaseContext, type: SystemToneType): Promise<SystemTonePlayer>--><!--Device-SystemSoundManager-getSystemTonePlayer(context: BaseContext, type: SystemToneType): Promise<SystemTonePlayer>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [SystemToneType](arkts-audio-systemsoundmanager-systemtonetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;SystemTonePlayer & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let type: systemSoundManager.SystemToneType = systemSoundManager.SystemToneType.SYSTEM_TONE_TYPE_SIM_CARD_0;
let systemTonePlayer: systemSoundManager.SystemTonePlayer | undefined = undefined;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getSystemTonePlayer(context, type).then((value: systemSoundManager.SystemTonePlayer) => {
  console.info('Succeeded in doing getSystemTonePlayer.');
    systemTonePlayer = value;
}).catch((err: BusinessError) => {
  console.error(`Failed to getSystemTonePlayer. Code: ${err.code}, message: ${err.message}`);
});
```

## getSystemToneUri

```TypeScript
getSystemToneUri(context: BaseContext, type: SystemToneType): Promise<string>
```

获取系统提示音uri。使用Promise异步回调。

**起始版本：** 11

<!--Device-SystemSoundManager-getSystemToneUri(context: BaseContext, type: SystemToneType): Promise<string>--><!--Device-SystemSoundManager-getSystemToneUri(context: BaseContext, type: SystemToneType): Promise<string>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [SystemToneType](arkts-audio-systemsoundmanager-systemtonetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let type: systemSoundManager.SystemToneType = systemSoundManager.SystemToneType.SYSTEM_TONE_TYPE_SIM_CARD_0;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getSystemToneUri(context, type).then((value: string) => {
  console.info('Succeeded in doing getSystemToneUri.');
}).catch((err: BusinessError) => {
  console.error(`Failed to getSystemToneUri. Code: ${err.code}, message: ${err.message}`);
});
```

## getToneHapticsList

```TypeScript
getToneHapticsList(context: BaseContext, isSynced: boolean): Promise<ToneHapticsAttrsArray>
```

获取同步或者非同步的系统铃音的振动属性列表。使用Promise异步回调。

**起始版本：** 14

<!--Device-SystemSoundManager-getToneHapticsList(context: BaseContext, isSynced: boolean): Promise<ToneHapticsAttrsArray>--><!--Device-SystemSoundManager-getToneHapticsList(context: BaseContext, isSynced: boolean): Promise<ToneHapticsAttrsArray>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| isSynced | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ToneHapticsAttrsArray](arkts-audio-systemsoundmanager-tonehapticsattrsarray-t.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [20700003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio-ringtone-sys.md#20700003-操作不支持) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getToneHapticsList(context, false).then((value: systemSoundManager.ToneHapticsAttrsArray) => {
  console.info('Succeeded in doing getToneHapticsList.');
}).catch((err: BusinessError) => {
  console.error(`Failed to getToneHapticsList. Code: ${err.code}, message: ${err.message}`);
});
```

## getToneHapticsSettings

```TypeScript
getToneHapticsSettings(context: BaseContext, type: ToneHapticsType): Promise<ToneHapticsSettings>
```

获取系统铃音的振动设置。使用Promise异步回调。

**起始版本：** 14

<!--Device-SystemSoundManager-getToneHapticsSettings(context: BaseContext, type: ToneHapticsType): Promise<ToneHapticsSettings>--><!--Device-SystemSoundManager-getToneHapticsSettings(context: BaseContext, type: ToneHapticsType): Promise<ToneHapticsSettings>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [ToneHapticsType](arkts-audio-systemsoundmanager-tonehapticstype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ToneHapticsSettings](arkts-audio-systemsoundmanager-tonehapticssettings-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [20700003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio-ringtone-sys.md#20700003-操作不支持) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let type: systemSoundManager.ToneHapticsType = systemSoundManager.ToneHapticsType.CALL_SIM_CARD_0;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getToneHapticsSettings(context, type).then((value: systemSoundManager.ToneHapticsSettings) => {
  console.info('Succeeded in doing getToneHapticsSettings.');
}).catch((err: BusinessError) => {
  console.error(`Failed to getToneHapticsSettings. Code: ${err.code}, message: ${err.message}`);
});
```

## openAlarmTone

```TypeScript
openAlarmTone(context: BaseContext, uri: string): Promise<number>
```

打开闹铃文件。使用Promise异步回调。

**起始版本：** 12

<!--Device-SystemSoundManager-openAlarmTone(context: BaseContext, uri: string): Promise<int>--><!--Device-SystemSoundManager-openAlarmTone(context: BaseContext, uri: string): Promise<int>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| 20700001 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let uri = 'file://data/test.wav'; // 需更改为目标铃声文件的uri。

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.openAlarmTone(context, uri).then((value: number) => {
  console.info('Succeeded in doing openAlarmTone.');
}).catch((err: BusinessError) => {
  console.error(`Failed to openAlarmTone. Code: ${err.code}, message: ${err.message}`);
});
```

## openToneHaptics

```TypeScript
openToneHaptics(context: BaseContext, hapticsUri: string): Promise<number>
```

打开系统铃音的振动。使用Promise异步回调。

**起始版本：** 14

<!--Device-SystemSoundManager-openToneHaptics(context: BaseContext, hapticsUri: string): Promise<int>--><!--Device-SystemSoundManager-openToneHaptics(context: BaseContext, hapticsUri: string): Promise<int>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| [hapticsUri](arkts-audio-systemsoundmanager-tonehapticssettings-i.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [20700003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio-ringtone-sys.md#20700003-操作不支持) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let hapticsUri = '/data/storage/el2/base/haptics/synchronized/alarms/test.json'; // 需更改为目标系统铃音的振动的uri。

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.openToneHaptics(context, hapticsUri).then((value: number) => {
  console.info('Succeeded in doing openToneHaptics.');
}).catch((err: BusinessError) => {
  console.error(`Failed to openToneHaptics. Code: ${err.code}, message: ${err.message}`);
});
```

## openToneList

```TypeScript
openToneList(uriList: Array<string>): Promise<Array<[string, number, SystemSoundError]>>
```

获取系统铃声的属性列表。使用Promise异步回调。

**起始版本：** 20

<!--Device-SystemSoundManager-openToneList(uriList: Array<string>): Promise<Array<[string, long, SystemSoundError]>>--><!--Device-SystemSoundManager-openToneList(uriList: Array<string>): Promise<Array<[string, long, SystemSoundError]>>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [uriList](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-cmresult-i.md) | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;[string, number, SystemSoundError] & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [20700007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio-ringtone-sys.md#20700007-参数无效) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let type: systemSoundManager.RingtoneType = systemSoundManager.RingtoneType.RINGTONE_TYPE_SIM_CARD_0;
let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();

systemSoundManagerInstance.getCurrentRingtoneAttribute(type).then((toneAttrs) => {
  console.info('Succeeded in getting current ringtone attribute.');
  systemSoundManagerInstance.openToneList([toneAttrs.getUri()]).then((value) => {
    console.info('Succeeded in opening tone list.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to open tone list. Code: ${err.code}, message: ${err.message}`);
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to get current ringtone attribute. Code: ${err.code}, message: ${err.message}`);
});
```

## removeCustomizedTone

```TypeScript
removeCustomizedTone(context: BaseContext, uri:string): Promise<void>
```

从铃音库中删除自定义铃音。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.WRITE_RINGTONE

<!--Device-SystemSoundManager-removeCustomizedTone(context: BaseContext, uri:string): Promise<void>--><!--Device-SystemSoundManager-removeCustomizedTone(context: BaseContext, uri:string): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let uri = 'file://data/test.wav'; // 需更改为目标铃声文件的uri。

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.removeCustomizedTone(context, uri).then(() => {
  console.info('Succeeded in doing removeCustomizedTone.');
}).catch((err: BusinessError) => {
  console.error(`Failed to removeCustomizedTone. Code: ${err.code}, message: ${err.message}`);
});
```

## removeCustomizedToneList

```TypeScript
removeCustomizedToneList(uriList: Array<string>): Promise<Array<[string, SystemSoundError]>>
```

批量删除自定义铃音列表。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.WRITE_RINGTONE

<!--Device-SystemSoundManager-removeCustomizedToneList(uriList: Array<string>): Promise<Array<[string, SystemSoundError]>>--><!--Device-SystemSoundManager-removeCustomizedToneList(uriList: Array<string>): Promise<Array<[string, SystemSoundError]>>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [uriList](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-cmresult-i.md) | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;[string, SystemSoundError] & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [20700007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio-ringtone-sys.md#20700007-参数无效) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let type: systemSoundManager.RingtoneType = systemSoundManager.RingtoneType.RINGTONE_TYPE_SIM_CARD_0;
let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();

systemSoundManagerInstance.getCurrentRingtoneAttribute(type).then((toneAttrs) => {
  console.info('Succeeded in getting current ringtone attribute.');
  systemSoundManagerInstance.removeCustomizedToneList([toneAttrs.getUri()]).then((value) => {
    console.info('Succeeded in using removeCustomizedToneList function.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to use removeCustomizedToneList function. Code: ${err.code}, message: ${err.message}`);
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to get current ringtone attribute. Code: ${err.code}, message: ${err.message}`);
});
```

## setAlarmToneUri

```TypeScript
setAlarmToneUri(context: BaseContext, uri: string): Promise<void>
```

设置系统闹铃uri。使用Promise异步回调。

**起始版本：** 12

<!--Device-SystemSoundManager-setAlarmToneUri(context: BaseContext, uri: string): Promise<void>--><!--Device-SystemSoundManager-setAlarmToneUri(context: BaseContext, uri: string): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| uri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| 20700001 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let uri = 'file://data/test.wav'; // 需更改为目标铃声文件的uri。

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.setAlarmToneUri(context, uri).then(() => {
  console.info('Succeeded in doing setAlarmToneUri.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setAlarmToneUri. Code: ${err.code}, message: ${err.message}`);
});
```

## setRingtoneUri

```TypeScript
setRingtoneUri(context: BaseContext, uri: string, type: RingtoneType): Promise<void>
```

设置系统铃声uri。使用Promise异步回调。

**起始版本：** 11

<!--Device-SystemSoundManager-setRingtoneUri(context: BaseContext, uri: string, type: RingtoneType): Promise<void>--><!--Device-SystemSoundManager-setRingtoneUri(context: BaseContext, uri: string, type: RingtoneType): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| uri | string | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let uri = 'file://data/test.wav'; // 需更改为目标铃声文件的uri。
let type: systemSoundManager.RingtoneType = systemSoundManager.RingtoneType.RINGTONE_TYPE_SIM_CARD_0;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.setRingtoneUri(context, uri, type).then(() => {
  console.info('Succeeded in doing setRingtoneUri.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setRingtoneUri. Code: ${err.code}, message: ${err.message}`);
});
```

## setSystemRingtoneUri

```TypeScript
setSystemRingtoneUri(context: Context, uri: string, type: RingtoneType, callback: AsyncCallback<void>): void
```

设置系统铃声uri。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [setRingtoneUri](#setRingtoneUri)

<!--Device-SystemSoundManager-setSystemRingtoneUri(context: Context, uri: string, type: RingtoneType, callback: AsyncCallback<void>): void--><!--Device-SystemSoundManager-setSystemRingtoneUri(context: Context, uri: string, type: RingtoneType, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| uri | string | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let uri = 'file://data/test.wav'; // 需更改为目标铃声文件的uri。
let type: systemSoundManager.RingtoneType = systemSoundManager.RingtoneType.RINGTONE_TYPE_DEFAULT;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.setSystemRingtoneUri(context, uri, type, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set system ringtone uri. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate a successful setting of the system ringtone uri.`);
});
```

## setSystemRingtoneUri

```TypeScript
setSystemRingtoneUri(context: Context, uri: string, type: RingtoneType): Promise<void>
```

设置系统铃声uri。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [setRingtoneUri](#setRingtoneUri)

<!--Device-SystemSoundManager-setSystemRingtoneUri(context: Context, uri: string, type: RingtoneType): Promise<void>--><!--Device-SystemSoundManager-setSystemRingtoneUri(context: Context, uri: string, type: RingtoneType): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| uri | string | 是 |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let uri = 'file://data/test.wav'; // 需更改为目标铃声文件的uri。
let type: systemSoundManager.RingtoneType = systemSoundManager.RingtoneType.RINGTONE_TYPE_DEFAULT;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.setSystemRingtoneUri(context, uri, type).then(() => {
  console.info('Succeeded in doing setSystemRingtoneUri.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setSystemRingtoneUri. Code: ${err.code}, message: ${err.message}`);
});
```

## setSystemToneUri

```TypeScript
setSystemToneUri(context: BaseContext, uri: string, type: SystemToneType): Promise<void>
```

设置系统提示音uri。使用Promise异步回调。

**起始版本：** 11

<!--Device-SystemSoundManager-setSystemToneUri(context: BaseContext, uri: string, type: SystemToneType): Promise<void>--><!--Device-SystemSoundManager-setSystemToneUri(context: BaseContext, uri: string, type: SystemToneType): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| uri | string | 是 |
| type | [SystemToneType](arkts-audio-systemsoundmanager-systemtonetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let uri = 'file://data/test.wav'; // 需更改为目标铃声文件的uri。
let type: systemSoundManager.SystemToneType = systemSoundManager.SystemToneType.SYSTEM_TONE_TYPE_SIM_CARD_0;

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.setSystemToneUri(context, uri, type).then(() => {
  console.info('Succeeded in doing setSystemToneUri.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setSystemToneUri. Code: ${err.code}, message: ${err.message}`);
});
```

## setToneHapticsSettings

```TypeScript
setToneHapticsSettings(context: BaseContext, type: ToneHapticsType, settings: ToneHapticsSettings): Promise<void>
```

设置系统铃音的振动。使用Promise异步回调。

**起始版本：** 14

<!--Device-SystemSoundManager-setToneHapticsSettings(context: BaseContext, type: ToneHapticsType, settings: ToneHapticsSettings): Promise<void>--><!--Device-SystemSoundManager-setToneHapticsSettings(context: BaseContext, type: ToneHapticsType, settings: ToneHapticsSettings): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | 是 |
| type | [ToneHapticsType](arkts-audio-systemsoundmanager-tonehapticstype-e.md) | 是 |
| settings | [ToneHapticsSettings](arkts-audio-systemsoundmanager-tonehapticssettings-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-media-kit/errorcode-media.md#5400103-出现io错误) |
| [20700003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-audio-kit/errorcode-audio-ringtone-sys.md#20700003-操作不支持) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let type: systemSoundManager.ToneHapticsType = systemSoundManager.ToneHapticsType.CALL_SIM_CARD_0;
let toneHapticsSettings: systemSoundManager.ToneHapticsSettings = {
  mode: systemSoundManager.ToneHapticsMode.NON_SYNC,
  hapticsUri: '/data/storage/el2/base/haptics/synchronized/alarms/test.json', // 需更改为通过getToneHapticsList获取的Uri。
}

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.setToneHapticsSettings(context, type, toneHapticsSettings).then(() => {
  console.info('Succeeded in doing setToneHapticsSettings.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setToneHapticsSettings. Code: ${err.code}, message: ${err.message}`);
});
```
