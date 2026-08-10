# canShowFloating

## 导入模块

```TypeScript
import { settings } from 'kits/@kit.BasicServicesKit';
```

## canShowFloating

```TypeScript
function canShowFloating(callback: AsyncCallback<boolean>): void
```

Checks whether a specified application can show as a floating window.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**废弃版本：** 26.0.0

<!--Device-settings-function canShowFloating(callback: AsyncCallback<boolean>): void--><!--Device-settings-function canShowFloating(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Applications.Settings.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 | The callback of canShowFloating result. |

## 示例

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

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**废弃版本：** 26.0.0

<!--Device-settings-function canShowFloating(): Promise<boolean>--><!--Device-settings-function canShowFloating(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Applications.Settings.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | Returns { |

## 示例

```TypeScript
settings.canShowFloating().then((status:boolean) => {
    console.info('Checks whether a specified application can show as float window.');
});
```

