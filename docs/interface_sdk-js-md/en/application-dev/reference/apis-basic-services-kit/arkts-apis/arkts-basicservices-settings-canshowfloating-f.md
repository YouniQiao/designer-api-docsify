# canShowFloating

## Modules to Import

```TypeScript
import { settings } from '@kit.BasicServicesKit';
import { settingsLite } from '@kit.BasicServicesKit';
```

## canShowFloating

```TypeScript
function canShowFloating(callback: AsyncCallback<boolean>): void
```

Checks whether a specified application can show as a floating window.

**Since:** 23

**Deprecated since:** 26.0.0

<!--Device-settings-function canShowFloating(callback: AsyncCallback<boolean>): void--><!--Device-settings-function canShowFloating(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-asynccallback-t.md)&lt;boolean&gt; | Yes | The callback of canShowFloating result. |

**Examples**

```TypeScript
settings.canShowFloating((err:Error, status: boolean) => {
  if (err) {
    console.error(`Failed to Checks whether a specified application can show as float window ${err.message} `);
    return;
  }
  console.info('Checks whether a specified application can show as float window.');
});
```


## canShowFloating

```TypeScript
function canShowFloating(): Promise<boolean>
```

Checks whether a specified application can show as a floating window.

**Since:** 23

**Deprecated since:** 26.0.0

<!--Device-settings-function canShowFloating(): Promise<boolean>--><!--Device-settings-function canShowFloating(): Promise<boolean>-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Returns { |

**Examples**

```TypeScript
settings.canShowFloating().then((status:boolean) => {
    console.info('Checks whether a specified application can show as float window.');
});
```

