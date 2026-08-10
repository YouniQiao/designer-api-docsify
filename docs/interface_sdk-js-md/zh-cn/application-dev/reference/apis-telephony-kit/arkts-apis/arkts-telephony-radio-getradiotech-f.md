# getRadioTech

## 导入模块

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## getRadioTech

```TypeScript
function getRadioTech(slotId: int, callback: AsyncCallback<NetworkRadioTech>): void
```

Obtains radio access technology (RAT) of the registered network. The system returns RAT of the packet service (PS) and circuit service (CS) domain.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_NETWORK_INFO

<!--Device-radio-function getRadioTech(slotId: int, callback: AsyncCallback<NetworkRadioTech>): void--><!--Device-radio-function getRadioTech(slotId: int, callback: AsyncCallback<NetworkRadioTech>): void-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;NetworkRadioTech&gt; | 是 | Returns the RAT of PS domain and CS domain of registered network. The values of RAT are as follows: &lt;ul&gt; &lt;li&gt;{@code RadioTechnology#RADIO_TECHNOLOGY_UNKNOWN} &lt;li&gt;{@code RadioTechnology#RADIO_TECHNOLOGY_GSM} &lt;li&gt;{@code RadioTechnology#RADIO_TECHNOLOGY_1XRTT} &lt;li&gt;{@code RadioTechnology#RADIO_TECHNOLOGY_WCDMA} &lt;li&gt;{@code RadioTechnology#RADIO_TECHNOLOGY_HSPA} &lt;li&gt;{@code RadioTechnology#RADIO_TECHNOLOGY_HSPAP} &lt;li&gt;{@code RadioTechnology#RADIO_TECHNOLOGY_TD_SCDMA} &lt;li&gt;{@code RadioTechnology#RADIO_TECHNOLOGY_EVDO} &lt;li&gt;{@code RadioTechnology#RADIO_TECHNOLOGY_EHRPD} &lt;li&gt;{@code RadioTechnology#RADIO_TECHNOLOGY_LTE} &lt;li&gt;{@code RadioTechnology#RADIO_TECHNOLOGY_LTE_CA} &lt;li&gt;{@code RadioTechnology#RADIO_TECHNOLOGY_IWLAN} &lt;li&gt;{@code RadioTechnology#RADIO_TECHNOLOGY_NR} &lt;/ul&gt; |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 8300999 | Unknown error. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |


## getRadioTech

```TypeScript
function getRadioTech(slotId: int): Promise<NetworkRadioTech>
```

Obtains radio access technology (RAT) of the registered network. The system returns RAT of the packet service (PS) and circuit service (CS) domain.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.GET_NETWORK_INFO

<!--Device-radio-function getRadioTech(slotId: int): Promise<NetworkRadioTech>--><!--Device-radio-function getRadioTech(slotId: int): Promise<NetworkRadioTech>-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;NetworkRadioTech&gt; | Returns the RAT of PS domain and CS domain of registered network. The values of RAT are as follows: &lt;ul&gt; &lt;li&gt;{ |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 8300999 | Unknown error. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

