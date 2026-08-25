# @ohos.app.form.formObserver(formObserver)

formObserver模块提供了卡片监听方相关接口的能力，包括对同一用户下安装的卡片新增、删除、可见性变化事件的订阅和取消订阅，获取正在运行的卡片信息等。

> **说明：**&gt;
> 本模块接口均为系统接口。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { formObserver } from '@kit.FormKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getRunningFormInfoById(formObserver)](arkts-form-formobserver-getrunningforminfobyid-f-sys.md) |
| [getRunningFormInfoById(formObserver)](arkts-form-formobserver-getrunningforminfobyid-f-sys.md) |
| [getRunningFormInfoById(formObserver)](arkts-form-formobserver-getrunningforminfobyid-f-sys.md) |
| [getRunningFormInfoById(formObserver)](arkts-form-formobserver-getrunningforminfobyid-f-sys.md) |
| [getRunningFormInfos(formObserver)](arkts-form-formobserver-getrunningforminfos-f-sys.md) |
| [getRunningFormInfos(formObserver)](arkts-form-formobserver-getrunningforminfos-f-sys.md) |
| [getRunningFormInfos(formObserver)](arkts-form-formobserver-getrunningforminfos-f-sys.md) |
| [getRunningFormInfos(formObserver)](arkts-form-formobserver-getrunningforminfos-f-sys.md) |
| [getRunningFormInfosByFilter(formObserver)](arkts-form-formobserver-getrunningforminfosbyfilter-f-sys.md) |
| [getRunningFormInfosByFilter(formObserver)](arkts-form-formobserver-getrunningforminfosbyfilter-f-sys.md) |
| [off(formObserver)](arkts-form-formobserver-off-f-sys.md#offformadd) |
| [off(formObserver)](arkts-form-formobserver-off-f-sys.md#offformremove) |
| [off(formObserver)](arkts-form-formobserver-off-f-sys.md#offnotifyvisible) |
| [off(formObserver)](arkts-form-formobserver-off-f-sys.md#offnotifyinvisible) |
| [off(formObserver)](arkts-form-formobserver-off-f-sys.md#offrouter) |
| [off(formObserver)](arkts-form-formobserver-off-f-sys.md#offmessage) |
| [off(formObserver)](arkts-form-formobserver-off-f-sys.md#offcall) |
| [offCall(formObserver)](arkts-form-formobserver-offcall-f-sys.md) |
| [offFormAdd(formObserver)](arkts-form-formobserver-offformadd-f-sys.md) |
| [offFormRemove(formObserver)](arkts-form-formobserver-offformremove-f-sys.md) |
| [offMessage(formObserver)](arkts-form-formobserver-offmessage-f-sys.md) |
| [offNotifyInvisible(formObserver)](arkts-form-formobserver-offnotifyinvisible-f-sys.md) |
| [offNotifyVisible(formObserver)](arkts-form-formobserver-offnotifyvisible-f-sys.md) |
| [offRouter(formObserver)](arkts-form-formobserver-offrouter-f-sys.md) |
| [on(formObserver)](arkts-form-formobserver-on-f-sys.md#onformadd) |
| [on(formObserver)](arkts-form-formobserver-on-f-sys.md#onformadd) |
| [on(formObserver)](arkts-form-formobserver-on-f-sys.md#onformremove) |
| [on(formObserver)](arkts-form-formobserver-on-f-sys.md#onformremove) |
| [on(formObserver)](arkts-form-formobserver-on-f-sys.md#onnotifyvisible) |
| [on(formObserver)](arkts-form-formobserver-on-f-sys.md#onnotifyvisible) |
| [on(formObserver)](arkts-form-formobserver-on-f-sys.md#onnotifyinvisible) |
| [on(formObserver)](arkts-form-formobserver-on-f-sys.md#onnotifyinvisible) |
| [on(formObserver)](arkts-form-formobserver-on-f-sys.md#onrouter) |
| [on(formObserver)](arkts-form-formobserver-on-f-sys.md#onrouter) |
| [on(formObserver)](arkts-form-formobserver-on-f-sys.md#onmessage) |
| [on(formObserver)](arkts-form-formobserver-on-f-sys.md#onmessage) |
| [on(formObserver)](arkts-form-formobserver-on-f-sys.md#oncall) |
| [on(formObserver)](arkts-form-formobserver-on-f-sys.md#oncall) |
| [onCall(formObserver)](arkts-form-formobserver-oncall-f-sys.md) |
| [onCall(formObserver)](arkts-form-formobserver-oncall-f-sys.md) |
| [onFormAdd(formObserver)](arkts-form-formobserver-onformadd-f-sys.md) |
| [onFormAdd(formObserver)](arkts-form-formobserver-onformadd-f-sys.md) |
| [onFormRemove(formObserver)](arkts-form-formobserver-onformremove-f-sys.md) |
| [onFormRemove(formObserver)](arkts-form-formobserver-onformremove-f-sys.md) |
| [onMessage(formObserver)](arkts-form-formobserver-onmessage-f-sys.md) |
| [onMessage(formObserver)](arkts-form-formobserver-onmessage-f-sys.md) |
| [onNotifyInvisible(formObserver)](arkts-form-formobserver-onnotifyinvisible-f-sys.md) |
| [onNotifyInvisible(formObserver)](arkts-form-formobserver-onnotifyinvisible-f-sys.md) |
| [onNotifyVisible(formObserver)](arkts-form-formobserver-onnotifyvisible-f-sys.md) |
| [onNotifyVisible(formObserver)](arkts-form-formobserver-onnotifyvisible-f-sys.md) |
| [onRouter(formObserver)](arkts-form-formobserver-onrouter-f-sys.md) |
| [onRouter(formObserver)](arkts-form-formobserver-onrouter-f-sys.md) |
<!--DelEnd-->
