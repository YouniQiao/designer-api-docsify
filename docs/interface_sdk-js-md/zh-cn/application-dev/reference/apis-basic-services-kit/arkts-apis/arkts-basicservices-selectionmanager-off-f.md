# off

## 导入模块

```TypeScript
import { selectionManager } from 'kits/@kit.BasicServicesKit';
```

## off('selectionCompleted')

```TypeScript
function off(type: 'selectionCompleted', callback?: Callback<SelectionInfo>): void
```

取消订阅划词完成事件，与 on('selectionCompleted') 搭配使用。

**起始版本：** 24

**系统能力：** SystemCapability.SelectionInput.Selection

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'selectionCompleted' | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i.md)&gt; | 否 |
