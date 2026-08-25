# MediaQueryListener

媒体查询的句柄，并包含了申请句柄时的首次查询结果。媒体查询根据设置的条件语句，比如'(width &lt;= 600vp)'，比较系统信息，若首次查询时相关信息未初始化，matches返回false。继承自[MediaQueryResult](arkts-arkui-mediaquery-mediaqueryresult-i.md)。

**继承/实现关系：** MediaQueryListener extends [MediaQueryResult](arkts-arkui-mediaquery-mediaqueryresult-i.md)

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { mediaquery } from 'kits/@kit.ArkUI';
```

## off('change')

```TypeScript
off(type: 'change', callback?: Callback<MediaQueryResult>): void
```

通过句柄向对应的查询条件取消注册回调，当媒体属性发生变更时不再触发指定的回调。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MediaQueryResult](arkts-arkui-mediaquery-mediaqueryresult-i.md)&gt; | 否 |

## on('change')

```TypeScript
on(type: 'change', callback: Callback<MediaQueryResult>): void
```

通过句柄向对应的查询条件注册回调，当媒体属性发生变更时会触发该回调。

> **说明：**&gt;
> 注册的回调中不允许进一步调用on或off。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MediaQueryResult](arkts-arkui-mediaquery-mediaqueryresult-i.md)&gt; | 是 |
