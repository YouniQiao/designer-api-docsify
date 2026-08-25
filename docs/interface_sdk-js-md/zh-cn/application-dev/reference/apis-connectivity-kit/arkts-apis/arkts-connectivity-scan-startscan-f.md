# startScan

## 导入模块

```TypeScript
import { scan } from '@kit.ConnectivityKit';
```

## startScan

```TypeScript
function startScan(filters: ScanFilters[] | null, options?: ScanOptions): Promise<void>
```

发起星闪扫描。使用Promise异步回调。需先调用[scan.onDeviceFound](arkts-connectivity-scan-ondevicefound-f.md)订阅扫描结果回调，本接口发起扫描后，扫描到的设备信息通过 [scan.onDeviceFound](arkts-connectivity-scan-ondevicefound-f.md)回调上报。扫描完成后可调用[scan.stopScan](arkts-connectivity-scan-stopscan-f.md)停止扫描。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filters | [ScanFilters](arkts-connectivity-scan-scanfilters-i.md)[] \| null | 是 |
| options | [ScanOptions](arkts-connectivity-scan-scanoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [36100003](../errorcode-nearlink-service.md#36100003-星闪关闭) |
| [36100040](../errorcode-nearlink-service.md#36100040-整数超出范围) |
| [36100041](../errorcode-nearlink-service.md#36100041-无效地址) |
| [36100042](../errorcode-nearlink-service.md#36100042-数组为空) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
