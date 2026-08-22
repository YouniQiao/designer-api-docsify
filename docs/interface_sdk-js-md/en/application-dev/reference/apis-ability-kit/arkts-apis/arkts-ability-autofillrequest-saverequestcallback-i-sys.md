# SaveRequestCallback (System API)

Implements callbacks for an automatic or a manual saving request.

**Since:** 23

<!--Device-unnamed-export interface SaveRequestCallback--><!--Device-unnamed-export interface SaveRequestCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

## onFailure

```TypeScript
onFailure(): void
```

Called when a saving request fails to be processed.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-SaveRequestCallback-onFailure(): void--><!--Device-SaveRequestCallback-onFailure(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |

**Examples**

```TypeScript
// MyAutoFillExtensionAbility.ts
import { AutoFillExtensionAbility, UIExtensionContentSession, autoFillManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyAutoFillExtensionAbility extends AutoFillExtensionAbility {
  onFillRequest(session: UIExtensionContentSession,
    request: autoFillManager.FillRequest,
    callback: autoFillManager.FillRequestCallback) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'autofill onFillRequest');
    try {
      let storageData: Record<string, string | autoFillManager.FillRequestCallback | autoFillManager.ViewData> = {
        'fillCallback': callback,
        'message': 'AutoFill Page',
        'viewData': request.viewData,
      }
      let storage_fill = new LocalStorage(storageData);
      if (session) {
        session.loadContent('pages/AutoFill Page', storage_fill);
      } else {
        hilog.error(0x0000, 'testTag', '%{public}s', 'session is null');
      }
    } catch (err) {
      hilog.error(0x0000, 'testTag', '%{public}s', 'failed to load content');
    }
  }
}
```

```TypeScript
// AutoFillPage.ets
import { autoFillManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct AutoFillPage {
  storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
  fillCallback: autoFillManager.FillRequestCallback | undefined =
    this.storage?.get<autoFillManager.FillRequestCallback>('fillCallback');
  
  build() {
    Row() {
      Column() {
        Text('AutoFill Page')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }

      Button('onFailure')
        .onClick(() => {
          hilog.info(0x0000, 'testTag', 'autofill failure');
          try {
            this.fillCallback?.onFailure();
          } catch (error) {
            console.error(`catch error, code: ${(error as BusinessError).code},
              message: ${(error as BusinessError).message}`);
          }
        })
        .width('100%')
    }
    .height('100%')
  }
}
```

```TypeScript
// MyAutoFillExtensionAbility.ts
import { AutoFillExtensionAbility, UIExtensionContentSession, autoFillManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyAutoFillExtensionAbility extends AutoFillExtensionAbility {
  onSaveRequest(session: UIExtensionContentSession,
    request: autoFillManager.SaveRequest,
    callback: autoFillManager.SaveRequestCallback) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'onSaveRequest');
    try {
      let storageData: Record<string, string | autoFillManager.SaveRequestCallback | autoFillManager.ViewData> = {
        'message': 'AutoFill Page',
        'saveCallback': callback,
        'viewData': request.viewData
      }
      let storage_save = new LocalStorage(storageData);
      if (session) {
        session.loadContent('pages/SavePage', storage_save);
      } else {
        hilog.error(0x0000, 'testTag', '%{public}s', 'session is null');
      }
    } catch (err) {
      hilog.error(0x0000, 'testTag', '%{public}s', 'failed to load content');
    }
  }
}
```

```TypeScript
// SavePage.ets
import { autoFillManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct SavePage {
  storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
  saveCallback: autoFillManager.SaveRequestCallback | undefined =
    this.storage?.get<autoFillManager.SaveRequestCallback>('saveCallback');

  build() {
    Row() {
      Column() {
        Text('Save Page')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }

      Button('onFailure')
        .onClick(() => {
          hilog.error(0x0000, 'testTag', 'autofill onFailure');
          try {
            this.saveCallback?.onFailure();
          } catch (error) {
            console.error(`catch error, code: ${(error as BusinessError).code},
              message: ${(error as BusinessError).message}`);
          }
        })
        .width('100%')
    }
    .height('100%')
  }
}
```

## onSuccess

```TypeScript
onSuccess(): void
```

Called when a saving request is successfully processed.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-SaveRequestCallback-onSuccess(): void--><!--Device-SaveRequestCallback-onSuccess(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |
| [16000050](../errorcode-ability.md#16000050-internal-error) | Internal error. |

**Examples**

```TypeScript
// MyAutoFillExtensionAbility.ts
import { AutoFillExtensionAbility, UIExtensionContentSession, autoFillManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyAutoFillExtensionAbility extends AutoFillExtensionAbility {
  onFillRequest(session: UIExtensionContentSession,
    request: autoFillManager.FillRequest,
    callback: autoFillManager.FillRequestCallback) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'autofill onFillRequest');
    try {
      let storageData: Record<string, string | autoFillManager.FillRequestCallback | autoFillManager.ViewData> = {
        'fillCallback': callback,
        'message': 'AutoFill Page',
        'viewData': request.viewData,
      }
      let storage_fill = new LocalStorage(storageData);
      if (session) {
        session.loadContent('pages/AutoFillPage', storage_fill);
      } else {
        hilog.error(0x0000, 'testTag', '%{public}s', 'session is null');
      }
    } catch (err) {
      hilog.error(0x0000, 'testTag', '%{public}s', 'failed to load content');
    }
  }
}
```

```TypeScript
// AutoFillPage.ets
import { autoFillManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct AutoFillPage {
  storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
  fillCallback: autoFillManager.FillRequestCallback | undefined =
    this.storage?.get<autoFillManager.FillRequestCallback>('fillCallback');
  viewData: autoFillManager.ViewData | undefined = this.storage?.get<autoFillManager.ViewData>('viewData');

  build() {
    Row() {
      Column() {
        Text('AutoFill Page')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }

      Button('onSuccess')
        .onClick(() => {
          if (this.viewData) {
            this.viewData.pageNodeInfos[0].value = 'user1';
            this.viewData.pageNodeInfos[1].value = 'user1 password';
            this.viewData.pageNodeInfos[2].value = 'user1 generate new password';
            hilog.info(0x0000, 'testTag', 'autofill success with viewData: %{public}s', JSON.stringify(this.viewData));
            try {
              this.fillCallback?.onSuccess({ viewData: this.viewData });
            } catch (error) {
              console.error(`catch error, code: ${(error as BusinessError).code},
                  message: ${(error as BusinessError).message}`);
            }
          }
        })
        .width('100%')
    }
    .height('100%')
  }
}
```

```TypeScript
// MyAutoFillExtensionAbility.ts
import { AutoFillExtensionAbility, UIExtensionContentSession, autoFillManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyAutoFillExtensionAbility extends AutoFillExtensionAbility {
  onSaveRequest(session: UIExtensionContentSession,
    request: autoFillManager.SaveRequest,
    callback: autoFillManager.SaveRequestCallback) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'onSaveRequest');
    try {
      let storageData: Record<string, string | autoFillManager.SaveRequestCallback | autoFillManager.ViewData> = {
        'message': 'AutoFill Page',
        'saveCallback': callback,
        'viewData': request.viewData
      };
      let storage_save = new LocalStorage(storageData);
      if (session) {
        session.loadContent('pages/SavePage', storage_save);
      } else {
        hilog.error(0x0000, 'testTag', '%{public}s', 'session is null');
      }
    } catch (err) {
      hilog.error(0x0000, 'testTag', '%{public}s', 'failed to load content');
    }
  }
}
```

```TypeScript
// SavePage.ets
import { autoFillManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct SavePage {
  storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
  saveCallback: autoFillManager.SaveRequestCallback | undefined =
    this.storage?.get<autoFillManager.SaveRequestCallback>('saveCallback');

  build() {
    Row() {
      Column() {
        Text('SavePage')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }

      Button('onSuccess')
        .onClick(() => {
          hilog.info(0x0000, 'testTag', 'autosave success');
          try {
            this.saveCallback?.onSuccess();
          } catch (error) {
            console.error(`catch error, code: ${(error as BusinessError).code},
                message: ${(error as BusinessError).message}`);
          }
        })
        .width('100%')
    }
    .height('100%')
  }
}
```

