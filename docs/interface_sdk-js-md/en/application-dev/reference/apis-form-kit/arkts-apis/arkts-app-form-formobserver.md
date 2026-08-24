# @ohos.app.form.formObserver

Interface of formObserver.@namespace formObserver

**Since:** 23

<!--Device-unnamed-declare namespace formObserver--><!--Device-unnamed-declare namespace formObserver-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { formObserver } from '@kit.FormKit';
```

## Summary

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [getRunningFormInfoById](arkts-form-formobserver-getrunningforminfobyid-f-sys.md) | Obtains the RunningFormInfo object by formId. |
| [getRunningFormInfoById](arkts-form-formobserver-getrunningforminfobyid-f-sys.md) | Obtains the RunningFormInfo object by formId. |
| [getRunningFormInfoById](arkts-form-formobserver-getrunningforminfobyid-f-sys.md) | Obtains the RunningFormInfo object by formId. |
| [getRunningFormInfoById](arkts-form-formobserver-getrunningforminfobyid-f-sys.md) | Obtains the RunningFormInfo object by formId. |
| [getRunningFormInfos](arkts-form-formobserver-getrunningforminfos-f-sys.md) | Obtains the RunningFormInfo objects provided by a specific card host application on the device. |
| [getRunningFormInfos](arkts-form-formobserver-getrunningforminfos-f-sys.md) | Obtains the RunningFormInfo objects provided by a specific card host application on the device. |
| [getRunningFormInfos](arkts-form-formobserver-getrunningforminfos-f-sys.md) | Obtains the RunningFormInfo objects provided by a specific card host application on the device. |
| [getRunningFormInfos](arkts-form-formobserver-getrunningforminfos-f-sys.md) | Obtains the RunningFormInfo objects provided by a specific card host application on the device. |
| [getRunningFormInfosByFilter](arkts-form-formobserver-getrunningforminfosbyfilter-f-sys.md) | Obtains the RunningFormInfo objects by FormProviderFilter. |
| [getRunningFormInfosByFilter](arkts-form-formobserver-getrunningforminfosbyfilter-f-sys.md) | Obtains the RunningFormInfo objects by FormProviderFilter. |
| [off_call](arkts-form-formobserver-offcall-f-sys.md) | Unregister form call event Listening. |
| [off_formAdd](arkts-form-formobserver-offformadd-f-sys.md) | Cancels listening to the event of add form. <p>You can use this method to cancel listening to the event of add form.</p> |
| [off_formRemove](arkts-form-formobserver-offformremove-f-sys.md) | Cancels listening to the event of remove form. <p>You can use this method to cancel listening to the event of remove form.</p> |
| [off_message](arkts-form-formobserver-offmessage-f-sys.md) | Unregister form message event Listening. |
| [off_notifyInvisible](arkts-form-formobserver-offnotifyinvisible-f-sys.md) | Cancels listening to the event of notifyInvisible type change. <p>You can use this method to cancel listening to the event of notifyInvisible type change.</p> |
| [off_notifyVisible](arkts-form-formobserver-offnotifyvisible-f-sys.md) | Cancels listening to the event of notifyVisible type change. <p>You can use this method to cancel listening to the event of notifyVisible type change.</p> |
| [off_router](arkts-form-formobserver-offrouter-f-sys.md) | Unregister form router event Listening. |
| [offCall](arkts-form-formobserver-offcall-f-sys.md) | Unregister form call event Listening. |
| [offFormAdd](arkts-form-formobserver-offformadd-f-sys.md) | Cancels listening to the event of add form. <p>You can use this method to cancel listening to the event of add form.</p> |
| [offFormRemove](arkts-form-formobserver-offformremove-f-sys.md) | Cancels listening to the event of remove form. <p>You can use this method to cancel listening to the event of remove form.</p> |
| [offMessage](arkts-form-formobserver-offmessage-f-sys.md) | Unregister form message event Listening. |
| [offNotifyInvisible](arkts-form-formobserver-offnotifyinvisible-f-sys.md) | Cancels listening to the event of notifyInvisible type change. <p>You can use this method to cancel listening to the event of notifyInvisible type change.</p> |
| [offNotifyVisible](arkts-form-formobserver-offnotifyvisible-f-sys.md) | Cancels listening to the event of notifyVisible type change. <p>You can use this method to cancel listening to the event of notifyVisible type change.</p> |
| [offRouter](arkts-form-formobserver-offrouter-f-sys.md) | Unregister form router event Listening. |
| [on_call](arkts-form-formobserver-oncall-f-sys.md) | Call event listening in registered form. <p>This interface requires permission to receive callback.</p> |
| [on_call](arkts-form-formobserver-oncall-f-sys.md) | Call event listening in registered form. <p>This interface requires permission to receive callback.</p> |
| [on_formAdd](arkts-form-formobserver-onformadd-f-sys.md) | Listens to the event of add form. <p>You can use this method to listen to the event of add form.</p> |
| [on_formAdd](arkts-form-formobserver-onformadd-f-sys.md) | Listens to the event of add form. <p>You can use this method to listen to the event of add form for a particular card host.</p> |
| [on_formRemove](arkts-form-formobserver-onformremove-f-sys.md) | Listens to the event of remove form. <p>You can use this method to listen to the event of remove form.</p> |
| [on_formRemove](arkts-form-formobserver-onformremove-f-sys.md) | Listens to the event of remove form. <p>You can use this method to listen to the event of remove form for a particular card host.</p> |
| [on_message](arkts-form-formobserver-onmessage-f-sys.md) | Message event listening in registered form. <p>This interface requires permission to receive callback.</p> |
| [on_message](arkts-form-formobserver-onmessage-f-sys.md) | Message event listening in registered form. <p>This interface requires permission to receive callback.</p> |
| [on_notifyInvisible](arkts-form-formobserver-onnotifyinvisible-f-sys.md) | Listens to the event of notifyInvisible type change. <p>You can use this method to listen to the event of notifyInvisible type change.</p> |
| [on_notifyInvisible](arkts-form-formobserver-onnotifyinvisible-f-sys.md) | Listens to the event of notifyInvisible type change. <p>You can use this method to listen to the event of notifyInvisible type change for a particular card host.</p> |
| [on_notifyVisible](arkts-form-formobserver-onnotifyvisible-f-sys.md) | Listens to the event of notifyVisible type change. <p>You can use this method to listen to the event of notifyVisible type change.</p> |
| [on_notifyVisible](arkts-form-formobserver-onnotifyvisible-f-sys.md) | Listens to the event of notifyVisible type change. <p>You can use this method to listen to the event of notifyVisible type change for a particular card host.</p> |
| [on_router](arkts-form-formobserver-onrouter-f-sys.md) | Router event listening in registered form. <p>This interface requires permission to receive callback.</p> |
| [on_router](arkts-form-formobserver-onrouter-f-sys.md) | Router event listening in registered form. <p>This interface requires permission to receive callback.</p> |
| [onCall](arkts-form-formobserver-oncall-f-sys.md) | Call event listening in registered form. <p>This interface requires permission to receive callback.</p> |
| [onCall](arkts-form-formobserver-oncall-f-sys.md) | Call event listening in registered form. <p>This interface requires permission to receive callback.</p> |
| [onFormAdd](arkts-form-formobserver-onformadd-f-sys.md) | Listens to the event of add form. <p>You can use this method to listen to the event of add form.</p> |
| [onFormAdd](arkts-form-formobserver-onformadd-f-sys.md) | Listens to the event of add form. <p>You can use this method to listen to the event of add form for a particular card host.</p> |
| [onFormRemove](arkts-form-formobserver-onformremove-f-sys.md) | Listens to the event of remove form. <p>You can use this method to listen to the event of remove form.</p> |
| [onFormRemove](arkts-form-formobserver-onformremove-f-sys.md) | Listens to the event of remove form. <p>You can use this method to listen to the event of remove form for a particular card host.</p> |
| [onMessage](arkts-form-formobserver-onmessage-f-sys.md) | Message event listening in registered form. <p>This interface requires permission to receive callback.</p> |
| [onMessage](arkts-form-formobserver-onmessage-f-sys.md) | Message event listening in registered form. <p>This interface requires permission to receive callback.</p> |
| [onNotifyInvisible](arkts-form-formobserver-onnotifyinvisible-f-sys.md) | Listens to the event of notifyInvisible type change. <p>You can use this method to listen to the event of notifyInvisible type change.</p> |
| [onNotifyInvisible](arkts-form-formobserver-onnotifyinvisible-f-sys.md) | Listens to the event of notifyInvisible type change. <p>You can use this method to listen to the event of notifyInvisible type change for a particular card host.</p> |
| [onNotifyVisible](arkts-form-formobserver-onnotifyvisible-f-sys.md) | Listens to the event of notifyVisible type change. <p>You can use this method to listen to the event of notifyVisible type change.</p> |
| [onNotifyVisible](arkts-form-formobserver-onnotifyvisible-f-sys.md) | Listens to the event of notifyVisible type change. <p>You can use this method to listen to the event of notifyVisible type change for a particular card host.</p> |
| [onRouter](arkts-form-formobserver-onrouter-f-sys.md) | Router event listening in registered form. <p>This interface requires permission to receive callback.</p> |
| [onRouter](arkts-form-formobserver-onrouter-f-sys.md) | Router event listening in registered form. <p>This interface requires permission to receive callback.</p> |
<!--DelEnd-->

