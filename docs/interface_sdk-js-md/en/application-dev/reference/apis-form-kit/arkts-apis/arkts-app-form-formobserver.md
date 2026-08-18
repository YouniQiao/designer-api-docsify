# @ohos.app.form.formObserver

Interface of formObserver.

**Since:** 23

<!--Device-unnamed-declare namespace formObserver--><!--Device-unnamed-declare namespace formObserver-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { formObserver } from '@kit.FormKit';
import { formObserver } from '@kit.FormKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getRunningFormInfoById](arkts-form-formobserver-getrunningforminfobyid-f-sys.md#getrunningforminfobyid) | Obtains the RunningFormInfo object by formId. |
| [getRunningFormInfoById](arkts-form-formobserver-getrunningforminfobyid-f-sys.md#getrunningforminfobyid-system-api) | Obtains the RunningFormInfo object by formId. |
| [getRunningFormInfoById](arkts-form-formobserver-getrunningforminfobyid-f-sys.md#getrunningforminfobyid-system-api) | Obtains the RunningFormInfo object by formId. |
| [getRunningFormInfoById](arkts-form-formobserver-getrunningforminfobyid-f-sys.md#getrunningforminfobyid-system-api) | Obtains the RunningFormInfo object by formId. |
| [getRunningFormInfos](arkts-form-formobserver-getrunningforminfos-f-sys.md#getrunningforminfos) | Obtains the RunningFormInfo objects provided by a specific card host application on the device. |
| [getRunningFormInfos](arkts-form-formobserver-getrunningforminfos-f-sys.md#getrunningforminfos-system-api) | Obtains the RunningFormInfo objects provided by a specific card host application on the device. |
| [getRunningFormInfos](arkts-form-formobserver-getrunningforminfos-f-sys.md#getrunningforminfos-system-api) | Obtains the RunningFormInfo objects provided by a specific card host application on the device. |
| [getRunningFormInfos](arkts-form-formobserver-getrunningforminfos-f-sys.md#getrunningforminfos-system-api) | Obtains the RunningFormInfo objects provided by a specific card host application on the device. |
| [getRunningFormInfosByFilter](arkts-form-formobserver-getrunningforminfosbyfilter-f-sys.md#getrunningforminfosbyfilter) | Obtains the RunningFormInfo objects by FormProviderFilter. |
| [getRunningFormInfosByFilter](arkts-form-formobserver-getrunningforminfosbyfilter-f-sys.md#getrunningforminfosbyfilter-system-api) | Obtains the RunningFormInfo objects by FormProviderFilter. |
| [offCall](arkts-form-formobserver-offcall-f-sys.md#offcall) | Unregister form call event Listening. |
| [offFormAdd](arkts-form-formobserver-offformadd-f-sys.md#offformadd) | Cancels listening to the event of add form. &lt;p&gt;You can use this method to cancel listening to the event of add form.&lt;/p&gt; |
| [offFormRemove](arkts-form-formobserver-offformremove-f-sys.md#offformremove) | Cancels listening to the event of remove form. &lt;p&gt;You can use this method to cancel listening to the event of remove form.&lt;/p&gt; |
| [offMessage](arkts-form-formobserver-offmessage-f-sys.md#offmessage) | Unregister form message event Listening. |
| [offNotifyInvisible](arkts-form-formobserver-offnotifyinvisible-f-sys.md#offnotifyinvisible) | Cancels listening to the event of notifyInvisible type change. &lt;p&gt;You can use this method to cancel listening to the event of notifyInvisible type change.&lt;/p&gt; |
| [offNotifyVisible](arkts-form-formobserver-offnotifyvisible-f-sys.md#offnotifyvisible) | Cancels listening to the event of notifyVisible type change. &lt;p&gt;You can use this method to cancel listening to the event of notifyVisible type change.&lt;/p&gt; |
| [offRouter](arkts-form-formobserver-offrouter-f-sys.md#offrouter) | Unregister form router event Listening. |
| [off_call](arkts-form-formobserver-offcall-f-sys.md#offcall) | Unregister form call event Listening. |
| [off_formAdd](arkts-form-formobserver-offformadd-f-sys.md#offformadd) | Cancels listening to the event of add form. &lt;p&gt;You can use this method to cancel listening to the event of add form.&lt;/p&gt; |
| [off_formRemove](arkts-form-formobserver-offformremove-f-sys.md#offformremove) | Cancels listening to the event of remove form. &lt;p&gt;You can use this method to cancel listening to the event of remove form.&lt;/p&gt; |
| [off_message](arkts-form-formobserver-offmessage-f-sys.md#offmessage) | Unregister form message event Listening. |
| [off_notifyInvisible](arkts-form-formobserver-offnotifyinvisible-f-sys.md#offnotifyinvisible) | Cancels listening to the event of notifyInvisible type change. &lt;p&gt;You can use this method to cancel listening to the event of notifyInvisible type change.&lt;/p&gt; |
| [off_notifyVisible](arkts-form-formobserver-offnotifyvisible-f-sys.md#offnotifyvisible) | Cancels listening to the event of notifyVisible type change. &lt;p&gt;You can use this method to cancel listening to the event of notifyVisible type change.&lt;/p&gt; |
| [off_router](arkts-form-formobserver-offrouter-f-sys.md#offrouter) | Unregister form router event Listening. |
| [onCall](arkts-form-formobserver-oncall-f-sys.md#oncall) | Call event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [onCall](arkts-form-formobserver-oncall-f-sys.md#oncall-system-api) | Call event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [onFormAdd](arkts-form-formobserver-onformadd-f-sys.md#onformadd) | Listens to the event of add form. &lt;p&gt;You can use this method to listen to the event of add form.&lt;/p&gt; |
| [onFormAdd](arkts-form-formobserver-onformadd-f-sys.md#onformadd-system-api) | Listens to the event of add form. &lt;p&gt;You can use this method to listen to the event of add form for a particular card host.&lt;/p&gt; |
| [onFormRemove](arkts-form-formobserver-onformremove-f-sys.md#onformremove) | Listens to the event of remove form. &lt;p&gt;You can use this method to listen to the event of remove form.&lt;/p&gt; |
| [onFormRemove](arkts-form-formobserver-onformremove-f-sys.md#onformremove-system-api) | Listens to the event of remove form. &lt;p&gt;You can use this method to listen to the event of remove form for a particular card host.&lt;/p&gt; |
| [onMessage](arkts-form-formobserver-onmessage-f-sys.md#onmessage) | Message event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [onMessage](arkts-form-formobserver-onmessage-f-sys.md#onmessage-system-api) | Message event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [onNotifyInvisible](arkts-form-formobserver-onnotifyinvisible-f-sys.md#onnotifyinvisible) | Listens to the event of notifyInvisible type change. &lt;p&gt;You can use this method to listen to the event of notifyInvisible type change.&lt;/p&gt; |
| [onNotifyInvisible](arkts-form-formobserver-onnotifyinvisible-f-sys.md#onnotifyinvisible-system-api) | Listens to the event of notifyInvisible type change. &lt;p&gt;You can use this method to listen to the event of notifyInvisible type change for a particular card host.&lt;/p&gt; |
| [onNotifyVisible](arkts-form-formobserver-onnotifyvisible-f-sys.md#onnotifyvisible) | Listens to the event of notifyVisible type change. &lt;p&gt;You can use this method to listen to the event of notifyVisible type change.&lt;/p&gt; |
| [onNotifyVisible](arkts-form-formobserver-onnotifyvisible-f-sys.md#onnotifyvisible-system-api) | Listens to the event of notifyVisible type change. &lt;p&gt;You can use this method to listen to the event of notifyVisible type change for a particular card host.&lt;/p&gt; |
| [onRouter](arkts-form-formobserver-onrouter-f-sys.md#onrouter) | Router event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [onRouter](arkts-form-formobserver-onrouter-f-sys.md#onrouter-system-api) | Router event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [on_call](arkts-form-formobserver-oncall-f-sys.md#oncall) | Call event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [on_call](arkts-form-formobserver-oncall-f-sys.md#oncall-system-api) | Call event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [on_formAdd](arkts-form-formobserver-onformadd-f-sys.md#onformadd) | Listens to the event of add form. &lt;p&gt;You can use this method to listen to the event of add form.&lt;/p&gt; |
| [on_formAdd](arkts-form-formobserver-onformadd-f-sys.md#onformadd-system-api) | Listens to the event of add form. &lt;p&gt;You can use this method to listen to the event of add form for a particular card host.&lt;/p&gt; |
| [on_formRemove](arkts-form-formobserver-onformremove-f-sys.md#onformremove) | Listens to the event of remove form. &lt;p&gt;You can use this method to listen to the event of remove form.&lt;/p&gt; |
| [on_formRemove](arkts-form-formobserver-onformremove-f-sys.md#onformremove-system-api) | Listens to the event of remove form. &lt;p&gt;You can use this method to listen to the event of remove form for a particular card host.&lt;/p&gt; |
| [on_message](arkts-form-formobserver-onmessage-f-sys.md#onmessage) | Message event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [on_message](arkts-form-formobserver-onmessage-f-sys.md#onmessage-system-api) | Message event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [on_notifyInvisible](arkts-form-formobserver-onnotifyinvisible-f-sys.md#onnotifyinvisible) | Listens to the event of notifyInvisible type change. &lt;p&gt;You can use this method to listen to the event of notifyInvisible type change.&lt;/p&gt; |
| [on_notifyInvisible](arkts-form-formobserver-onnotifyinvisible-f-sys.md#onnotifyinvisible-system-api) | Listens to the event of notifyInvisible type change. &lt;p&gt;You can use this method to listen to the event of notifyInvisible type change for a particular card host.&lt;/p&gt; |
| [on_notifyVisible](arkts-form-formobserver-onnotifyvisible-f-sys.md#onnotifyvisible) | Listens to the event of notifyVisible type change. &lt;p&gt;You can use this method to listen to the event of notifyVisible type change.&lt;/p&gt; |
| [on_notifyVisible](arkts-form-formobserver-onnotifyvisible-f-sys.md#onnotifyvisible-system-api) | Listens to the event of notifyVisible type change. &lt;p&gt;You can use this method to listen to the event of notifyVisible type change for a particular card host.&lt;/p&gt; |
| [on_router](arkts-form-formobserver-onrouter-f-sys.md#onrouter) | Router event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
| [on_router](arkts-form-formobserver-onrouter-f-sys.md#onrouter-system-api) | Router event listening in registered form. &lt;p&gt;This interface requires permission to receive callback.&lt;/p&gt; |
<!--DelEnd-->

