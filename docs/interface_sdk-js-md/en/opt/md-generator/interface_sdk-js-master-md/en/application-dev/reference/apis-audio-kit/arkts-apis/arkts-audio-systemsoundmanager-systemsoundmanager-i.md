# SystemSoundManager

System sound manager object.

**Since:** 10

<!--Device-systemSoundManager-interface SystemSoundManager--><!--Device-systemSoundManager-interface SystemSoundManager-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

## Modules to Import

```TypeScript
import { systemSoundManager } from 'kits/@kit.AudioKit';
```

## addCustomizedTone

```TypeScript
addCustomizedTone(context: BaseContext, toneAttr: ToneAttrs, externalUri: string): Promise<string>
```

Add customized tone into ringtone library.

**Since:** 12

**Required permissions:** ohos.permission.WRITE_RINGTONE

<!--Device-SystemSoundManager-addCustomizedTone(context: BaseContext, toneAttr: ToneAttrs, externalUri: string): Promise<string>--><!--Device-SystemSoundManager-addCustomizedTone(context: BaseContext, toneAttr: ToneAttrs, externalUri: string): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| toneAttr | [ToneAttrs](arkts-audio-systemsoundmanager-toneattrs-i.md) | Yes |
| externalUri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [20700006](../errorcode-audio-ringtone-sys.md#20700006-insufficient-rom-space) |
| [20700005](../errorcode-audio-ringtone-sys.md#20700005-file-count-exceeds-the-upper-limit) |
| [20700004](../errorcode-audio-ringtone-sys.md#20700004-data-size-exceeds-the-upper-limit) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let title = 'test'; // Change it to the actual name.
let fileName = 'displayName_test'; // Change it to the actual file name.
let categoryValue = systemSoundManager.TONE_CATEGORY_ALARM;

let toneAttrs = systemSoundManager.createCustomizedToneAttrs();
toneAttrs.setTitle(title);
toneAttrs.setFileName(fileName);
toneAttrs.setCategory(categoryValue);

let path = 'file://data/test.ogg'; // Change it to the URI of the actual tone file.

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

Add customized tone into ringtone library.

**Since:** 12

**Required permissions:** ohos.permission.WRITE_RINGTONE

<!--Device-SystemSoundManager-addCustomizedTone(context: BaseContext, toneAttr: ToneAttrs, fd: int, offset?: long, length?: long)      : Promise<string>--><!--Device-SystemSoundManager-addCustomizedTone(context: BaseContext, toneAttr: ToneAttrs, fd: int, offset?: long, length?: long)      : Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| toneAttr | [ToneAttrs](arkts-audio-systemsoundmanager-toneattrs-i.md) | Yes |
| fd | number | Yes |
| offset | number | No |
| length | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [20700006](../errorcode-audio-ringtone-sys.md#20700006-insufficient-rom-space) |
| [20700005](../errorcode-audio-ringtone-sys.md#20700005-file-count-exceeds-the-upper-limit) |
| [20700004](../errorcode-audio-ringtone-sys.md#20700004-data-size-exceeds-the-upper-limit) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let title = 'test'; // Change it to the actual name.
let fileName = 'displayName_test'; // Change it to the actual file name.
let categoryValue = systemSoundManager.TONE_CATEGORY_ALARM;

let toneAttrs = systemSoundManager.createCustomizedToneAttrs();
toneAttrs.setTitle(title);
toneAttrs.setFileName(fileName);
toneAttrs.setCategory(categoryValue);

let fd = 10; // Set the FD of the target tone.
let offset = 0; // Set the offset.
let length = 50; // Set the data length.

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

Close fd.

**Since:** 12

<!--Device-SystemSoundManager-close(fd: int): Promise<void>--><!--Device-SystemSoundManager-close(fd: int): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fd | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let fd = 50; // Use the FD of the target alarm tone.

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

Gets attribute list of alarm tones.

**Since:** 12

<!--Device-SystemSoundManager-getAlarmToneAttrList(context: BaseContext): Promise<ToneAttrsArray>--><!--Device-SystemSoundManager-getAlarmToneAttrList(context: BaseContext): Promise<ToneAttrsArray>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ToneAttrsArray&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
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

Gets uri of the current alarm tone.

**Since:** 12

<!--Device-SystemSoundManager-getAlarmToneUri(context: BaseContext): Promise<string>--><!--Device-SystemSoundManager-getAlarmToneUri(context: BaseContext): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
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

Gets the ringtone attribute which is in use.

**Since:** 20

<!--Device-SystemSoundManager-getCurrentRingtoneAttribute(type: RingtoneType): Promise<ToneAttrs>--><!--Device-SystemSoundManager-getCurrentRingtoneAttribute(type: RingtoneType): Promise<ToneAttrs>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ToneAttrs&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

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

Gets attributes of the default alarm tone.

**Since:** 12

<!--Device-SystemSoundManager-getDefaultAlarmToneAttrs(context: BaseContext): Promise<ToneAttrs>--><!--Device-SystemSoundManager-getDefaultAlarmToneAttrs(context: BaseContext): Promise<ToneAttrs>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ToneAttrs&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
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

Gets attributes of the default ringtone.

**Since:** 12

<!--Device-SystemSoundManager-getDefaultRingtoneAttrs(context: BaseContext, type: RingtoneType): Promise<ToneAttrs>--><!--Device-SystemSoundManager-getDefaultRingtoneAttrs(context: BaseContext, type: RingtoneType): Promise<ToneAttrs>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ToneAttrs&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
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

Gets attributes of the default system tone.

**Since:** 12

<!--Device-SystemSoundManager-getDefaultSystemToneAttrs(context: BaseContext, type: SystemToneType): Promise<ToneAttrs>--><!--Device-SystemSoundManager-getDefaultSystemToneAttrs(context: BaseContext, type: SystemToneType): Promise<ToneAttrs>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| type | [SystemToneType](arkts-audio-systemsoundmanager-systemtonetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ToneAttrs&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
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

Get attributes of haptics which is synchronized with one tone. If no haptics is found, then the attributes in the returned ToneHapticsAttrs is empty.

**Since:** 14

<!--Device-SystemSoundManager-getHapticsAttrsSyncedWithTone(context: BaseContext, toneUri: string): Promise<ToneHapticsAttrs>--><!--Device-SystemSoundManager-getHapticsAttrsSyncedWithTone(context: BaseContext, toneUri: string): Promise<ToneHapticsAttrs>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| toneUri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ToneHapticsAttrs&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [20700003](../errorcode-audio-ringtone-sys.md#20700003-operation-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let toneUri: string = '/data/storage/el2/base/RingTone/alarms/test.ogg'; // Change it to the URI of the actual tone file.

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.getHapticsAttrsSyncedWithTone(context, toneUri).then((value: systemSoundManager.ToneHapticsAttrs) => {
  console.info('Succeeded in doing getHapticsAttrsSyncedWithTone.');
}).catch((err: BusinessError) => {
  console.error(`Failed to getHapticsAttrsSyncedWithTone. Code: ${err.code}, message: ${err.message}`);
});
```

## getMockHapticRingtonePlayer

```TypeScript
getMockHapticRingtonePlayer(context: BaseContext, hapticUri: string): Promise<RingtonePlayer | null>
```

Obtains a mock haptic ringtone player for playing vibration files and their corresponding mock haptic sound files. This API uses a promise to return the result.Before calling this interface, ensure that the incoming hapticUri actually exists in the system.Otherwise, exceptions and errors will occur, such as failure to play the matched haptic sound file.After obtaining the instance through this interface, actively call {@link RingtonePlayer#release} method of the ringtone player to release player resources when the service is terminated.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemSoundManager-getMockHapticRingtonePlayer(context: BaseContext, hapticUri: string): Promise<RingtonePlayer | null>--><!--Device-SystemSoundManager-getMockHapticRingtonePlayer(context: BaseContext, hapticUri: string): Promise<RingtonePlayer | null>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| hapticUri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;RingtonePlayer \| null&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [20700002](../errorcode-audio-ringtone-sys.md#20700002-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getMockHapticRingtonePlayer

```TypeScript
getMockHapticRingtonePlayer(context: BaseContext, type: RingtoneType, ringtoneUri: string): Promise<RingtonePlayer | null>
```

Obtains a mock haptic ringtone player for playing vibration files and their corresponding mock haptic sound files. This API uses a promise to return the result.Before calling this interface, ensure that the incoming ringtoneUri actually exists in the system.Otherwise, exceptions and errors will occur, such as failure to play the matched haptic sound file.After obtaining the instance through this interface, actively call {@link RingtonePlayer#release} method of the ringtone player to release player resources when the service is terminated.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemSoundManager-getMockHapticRingtonePlayer(context: BaseContext, type: RingtoneType, ringtoneUri: string): Promise<RingtonePlayer | null>--><!--Device-SystemSoundManager-getMockHapticRingtonePlayer(context: BaseContext, type: RingtoneType, ringtoneUri: string): Promise<RingtonePlayer | null>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | Yes |
| ringtoneUri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;RingtonePlayer \| null&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [20700002](../errorcode-audio-ringtone-sys.md#20700002-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getRingtoneAttrList

```TypeScript
getRingtoneAttrList(context: BaseContext, type: RingtoneType): Promise<ToneAttrsArray>
```

Gets attribute list of ringtones.

**Since:** 12

<!--Device-SystemSoundManager-getRingtoneAttrList(context: BaseContext, type: RingtoneType): Promise<ToneAttrsArray>--><!--Device-SystemSoundManager-getRingtoneAttrList(context: BaseContext, type: RingtoneType): Promise<ToneAttrsArray>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ToneAttrsArray&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
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

Gets the ringtone player.

**Since:** 11

<!--Device-SystemSoundManager-getRingtonePlayer(context: BaseContext, type: RingtoneType): Promise<RingtonePlayer>--><!--Device-SystemSoundManager-getRingtonePlayer(context: BaseContext, type: RingtoneType): Promise<RingtonePlayer>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;RingtonePlayer&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
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

Gets the ringtone uri.

**Since:** 11

<!--Device-SystemSoundManager-getRingtoneUri(context: BaseContext, type: RingtoneType): Promise<string>--><!--Device-SystemSoundManager-getRingtoneUri(context: BaseContext, type: RingtoneType): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
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

Gets the ringtone player.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [systemSoundManager.SystemSoundManager#getRingtonePlayer](arkts-audio-systemsoundmanager-systemsoundmanager-i.md#getringtoneplayer)

<!--Device-SystemSoundManager-getSystemRingtonePlayer(context: Context, type: RingtoneType, callback: AsyncCallback<RingtonePlayer>): void--><!--Device-SystemSoundManager-getSystemRingtonePlayer(context: Context, type: RingtoneType, callback: AsyncCallback<RingtonePlayer>): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;RingtonePlayer&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
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

Gets the ringtone player.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [systemSoundManager.SystemSoundManager#getRingtonePlayer](arkts-audio-systemsoundmanager-systemsoundmanager-i.md#getringtoneplayer)

<!--Device-SystemSoundManager-getSystemRingtonePlayer(context: Context, type: RingtoneType): Promise<RingtonePlayer>--><!--Device-SystemSoundManager-getSystemRingtonePlayer(context: Context, type: RingtoneType): Promise<RingtonePlayer>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;RingtonePlayer&gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
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

Gets the ringtone uri.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [systemSoundManager.SystemSoundManager#getRingtoneUri](arkts-audio-systemsoundmanager-systemsoundmanager-i.md#getringtoneuri)

<!--Device-SystemSoundManager-getSystemRingtoneUri(context: Context, type: RingtoneType, callback: AsyncCallback<string>): void--><!--Device-SystemSoundManager-getSystemRingtoneUri(context: Context, type: RingtoneType, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
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

Gets the ringtone uri.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [systemSoundManager.SystemSoundManager#getRingtoneUri](arkts-audio-systemsoundmanager-systemsoundmanager-i.md#getringtoneuri)

<!--Device-SystemSoundManager-getSystemRingtoneUri(context: Context, type: RingtoneType): Promise<string>--><!--Device-SystemSoundManager-getSystemRingtoneUri(context: Context, type: RingtoneType): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
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

Gets attribute list of alarm tones.

**Since:** 12

<!--Device-SystemSoundManager-getSystemToneAttrList(context: BaseContext, type: SystemToneType): Promise<ToneAttrsArray>--><!--Device-SystemSoundManager-getSystemToneAttrList(context: BaseContext, type: SystemToneType): Promise<ToneAttrsArray>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| type | [SystemToneType](arkts-audio-systemsoundmanager-systemtonetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ToneAttrsArray&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
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

Gets the system tone player.

**Since:** 11

<!--Device-SystemSoundManager-getSystemTonePlayer(context: BaseContext, type: SystemToneType): Promise<SystemTonePlayer>--><!--Device-SystemSoundManager-getSystemTonePlayer(context: BaseContext, type: SystemToneType): Promise<SystemTonePlayer>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| type | [SystemToneType](arkts-audio-systemsoundmanager-systemtonetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;SystemTonePlayer&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
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

Gets the system tone uri.

**Since:** 11

<!--Device-SystemSoundManager-getSystemToneUri(context: BaseContext, type: SystemToneType): Promise<string>--><!--Device-SystemSoundManager-getSystemToneUri(context: BaseContext, type: SystemToneType): Promise<string>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| type | [SystemToneType](arkts-audio-systemsoundmanager-systemtonetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
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

Get haptics list.

**Since:** 14

<!--Device-SystemSoundManager-getToneHapticsList(context: BaseContext, isSynced: boolean): Promise<ToneHapticsAttrsArray>--><!--Device-SystemSoundManager-getToneHapticsList(context: BaseContext, isSynced: boolean): Promise<ToneHapticsAttrsArray>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| isSynced | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ToneHapticsAttrsArray&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [20700003](../errorcode-audio-ringtone-sys.md#20700003-operation-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
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

Get haptics settings.

**Since:** 14

<!--Device-SystemSoundManager-getToneHapticsSettings(context: BaseContext, type: ToneHapticsType): Promise<ToneHapticsSettings>--><!--Device-SystemSoundManager-getToneHapticsSettings(context: BaseContext, type: ToneHapticsType): Promise<ToneHapticsSettings>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| type | [ToneHapticsType](arkts-audio-systemsoundmanager-tonehapticstype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;ToneHapticsSettings&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [20700003](../errorcode-audio-ringtone-sys.md#20700003-operation-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
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

Open alarm tone file.

**Since:** 12

<!--Device-SystemSoundManager-openAlarmTone(context: BaseContext, uri: string): Promise<int>--><!--Device-SystemSoundManager-openAlarmTone(context: BaseContext, uri: string): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 20700001 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let uri = 'file://data/test.wav'; // Change it to the URI of the target tone file.

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

Open haptics.

**Since:** 14

<!--Device-SystemSoundManager-openToneHaptics(context: BaseContext, hapticsUri: string): Promise<int>--><!--Device-SystemSoundManager-openToneHaptics(context: BaseContext, hapticsUri: string): Promise<int>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| hapticsUri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [20700003](../errorcode-audio-ringtone-sys.md#20700003-operation-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let hapticsUri = '/data/storage/el2/base/haptics/synchronized/alarms/test.json'; // Change it to the URI of the target haptics resource.

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

Open tone list in batch.

**Since:** 20

<!--Device-SystemSoundManager-openToneList(uriList: Array<string>): Promise<Array<[string, long, SystemSoundError]>>--><!--Device-SystemSoundManager-openToneList(uriList: Array<string>): Promise<Array<[string, long, SystemSoundError]>>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uriList | Array&lt;string&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[string, number, SystemSoundError]&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [20700007](../errorcode-audio-ringtone-sys.md#20700007-invalid-parameter) |

## Examples

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

Remove customized tone in ringtone library.

**Since:** 12

**Required permissions:** ohos.permission.WRITE_RINGTONE

<!--Device-SystemSoundManager-removeCustomizedTone(context: BaseContext, uri:string): Promise<void>--><!--Device-SystemSoundManager-removeCustomizedTone(context: BaseContext, uri:string): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let uri = 'file://data/test.wav'; // Change it to the URI of the target tone file.

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

Remove customized tone list in batch.

**Since:** 20

**Required permissions:** ohos.permission.WRITE_RINGTONE

<!--Device-SystemSoundManager-removeCustomizedToneList(uriList: Array<string>): Promise<Array<[string, SystemSoundError]>>--><!--Device-SystemSoundManager-removeCustomizedToneList(uriList: Array<string>): Promise<Array<[string, SystemSoundError]>>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uriList | Array&lt;string&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[string, SystemSoundError]&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [20700007](../errorcode-audio-ringtone-sys.md#20700007-invalid-parameter) |

## Examples

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

Sets uri of the current alarm tone.

**Since:** 12

<!--Device-SystemSoundManager-setAlarmToneUri(context: BaseContext, uri: string): Promise<void>--><!--Device-SystemSoundManager-setAlarmToneUri(context: BaseContext, uri: string): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 20700001 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let uri = 'file://data/test.wav'; // Change it to the URI of the target tone file.

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

Sets the ringtone uri to system.

**Since:** 11

<!--Device-SystemSoundManager-setRingtoneUri(context: BaseContext, uri: string, type: RingtoneType): Promise<void>--><!--Device-SystemSoundManager-setRingtoneUri(context: BaseContext, uri: string, type: RingtoneType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| uri | string | Yes |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let uri = 'file://data/test.wav'; // Change it to the URI of the target tone file.
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

Sets the ringtone uri to system.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [systemSoundManager.SystemSoundManager#setRingtoneUri](arkts-audio-systemsoundmanager-systemsoundmanager-i.md#setringtoneuri)

<!--Device-SystemSoundManager-setSystemRingtoneUri(context: Context, uri: string, type: RingtoneType, callback: AsyncCallback<void>): void--><!--Device-SystemSoundManager-setSystemRingtoneUri(context: Context, uri: string, type: RingtoneType, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| uri | string | Yes |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let uri = 'file://data/test.wav'; // Change it to the URI of the target tone file.
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

Sets the ringtone uri to system.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [systemSoundManager.SystemSoundManager#setRingtoneUri](arkts-audio-systemsoundmanager-systemsoundmanager-i.md#setringtoneuri)

<!--Device-SystemSoundManager-setSystemRingtoneUri(context: Context, uri: string, type: RingtoneType): Promise<void>--><!--Device-SystemSoundManager-setSystemRingtoneUri(context: Context, uri: string, type: RingtoneType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| uri | string | Yes |
| type | [RingtoneType](arkts-audio-systemsoundmanager-ringtonetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let uri = 'file://data/test.wav'; // Change it to the URI of the target tone file.
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

Sets the system tone uri to system.

**Since:** 11

<!--Device-SystemSoundManager-setSystemToneUri(context: BaseContext, uri: string, type: SystemToneType): Promise<void>--><!--Device-SystemSoundManager-setSystemToneUri(context: BaseContext, uri: string, type: SystemToneType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| uri | string | Yes |
| type | [SystemToneType](arkts-audio-systemsoundmanager-systemtonetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let uri = 'file://data/test.wav'; // Change it to the URI of the target tone file.
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

Set haptics settings.

**Since:** 14

<!--Device-SystemSoundManager-setToneHapticsSettings(context: BaseContext, type: ToneHapticsType, settings: ToneHapticsSettings): Promise<void>--><!--Device-SystemSoundManager-setToneHapticsSettings(context: BaseContext, type: ToneHapticsType, settings: ToneHapticsSettings): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md) | Yes |
| type | [ToneHapticsType](arkts-audio-systemsoundmanager-tonehapticstype-e.md) | Yes |
| settings | [ToneHapticsSettings](arkts-audio-systemsoundmanager-tonehapticssettings-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5400102](../../apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [20700003](../errorcode-audio-ringtone-sys.md#20700003-operation-not-supported) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let type: systemSoundManager.ToneHapticsType = systemSoundManager.ToneHapticsType.CALL_SIM_CARD_0;
let toneHapticsSettings: systemSoundManager.ToneHapticsSettings = {
  mode: systemSoundManager.ToneHapticsMode.NON_SYNC,
  hapticsUri: '/data/storage/el2/base/haptics/synchronized/alarms/test.json', // Change it to the URI obtained through getToneHapticsList.
}

let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
systemSoundManagerInstance.setToneHapticsSettings(context, type, toneHapticsSettings).then(() => {
  console.info('Succeeded in doing setToneHapticsSettings.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setToneHapticsSettings. Code: ${err.code}, message: ${err.message}`);
});
```
