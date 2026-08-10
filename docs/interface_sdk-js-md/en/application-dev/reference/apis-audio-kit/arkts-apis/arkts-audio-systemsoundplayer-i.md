# SystemSoundPlayer

音效播放器提供了加载、卸载和播放系统声音的功能。

SystemSoundPlayer需要和  
[@ohos.multimedia.systemSoundManager](arkts-multimedia-systemsoundmanager.md)配合使用，才能完成管理系统音效的功能。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export interface SystemSoundPlayer--><!--Device-unnamed-export interface SystemSoundPlayer-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

## load

```TypeScript
load(soundType: systemSoundManager.SystemSoundType): Promise<void>
```

加载系统音效。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemSoundPlayer-load(soundType: systemSoundManager.SystemSoundType): Promise<void>--><!--Device-SystemSoundPlayer-load(soundType: systemSoundManager.SystemSoundType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| soundType | systemSoundManager.SystemSoundType | Yes | 系统音效类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400103 | I/O error. |
| 5400105 | Crash or blocking occurs in system process. |
| 5400108 | Parameter check failed. Returned by promise. |

## play

```TypeScript
play(soundType: systemSoundManager.SystemSoundType): Promise<void>
```

播放系统音效。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemSoundPlayer-play(soundType: systemSoundManager.SystemSoundType): Promise<void>--><!--Device-SystemSoundPlayer-play(soundType: systemSoundManager.SystemSoundType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| soundType | systemSoundManager.SystemSoundType | Yes | 系统音效类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400103 | I/O error. |
| 5400105 | Crash or blocking occurs in system process. |
| 5400108 | Parameter check failed. Returned by promise. |

## release

```TypeScript
release(): Promise<void>
```

释放系统音效播放器。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemSoundPlayer-release(): Promise<void>--><!--Device-SystemSoundPlayer-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400105 | Crash or blocking occurs in system process. |

## unload

```TypeScript
unload(soundType: systemSoundManager.SystemSoundType): Promise<void>
```

卸载之前已加载的系统音效。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemSoundPlayer-unload(soundType: systemSoundManager.SystemSoundType): Promise<void>--><!--Device-SystemSoundPlayer-unload(soundType: systemSoundManager.SystemSoundType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| soundType | systemSoundManager.SystemSoundType | Yes | 系统音效类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400105 | Crash or blocking occurs in system process. |
| 5400108 | Parameter check failed. Returned by promise. |

