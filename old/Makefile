.DEFAULT_GOAL = interactive

# Ambiente
R_HOME  = "$(shell R RHOME)"
RSCRIPT = "$(R_HOME)/bin/Rscript"
R       = "${R_HOME}/bin/R --no-save --no-restore --quiet"

BROWSER = firefox
SUBEDITOR = aegisub-3.2
EDITOR = emacs -nw
RM = rm -rf

# Default project infos
PRJ     = test
# PRJ     = gymix
# YT_ID   = lw53nODhRXU
#lunghezza chunks di sottotitoli per splitting in minuti
CHUNKS_LEN_MINS = 5
#quanti translate completi per creare una revisione?
TRN_TO_REV_RATIO = 6
# es con il setup CHUNKS_LEN_MINS = 5 e TRN_TO_REV_RATIO = 6 una revisione è
# di 30 minuti e ingloba 6 translate di 5 minuti ciascuno

interactive:
	python projects/${PRJ}.py

interactive-old:
	$(EDITOR) projects/${PRJ}.R

# tests:
# 	$(EDITOR) Makefile projects/test.R

# ------------------------------------------------
# Utilities database utenti
# ------------------------------------------------
edit-users-db:
	$(EDITOR) data/users.csv ~/src/rpkg/lbprivee/rawdata/av_yt_users.csv

# stampa il db
list-users:
	${RSCRIPT} -e \
	'usr <- lbav2::users$$new("data/users.csv"); usr$$print()' \
	| less

# lista revisori abilitati
summon-revisors:
	${RSCRIPT} -e \
	'usr <- lbav2::users$$new("data/users.csv"); usr$$mention("revisor2")'\
	| less

# ------------------------------------------------
# Utilities utenti di uno specifico progetto
# ------------------------------------------------

# lista persone assegnatarie di spezzoni per un determinato progetto
list-assignee:
	${RSCRIPT} -e \
	'lbav2::prj$$new(id = "$(PRJ)", yt_id = "$(YT_ID)")$$list_assignee()' | less

# ---------------------------------------------------------------------------
# Setup del progetto (splitting source e setup file monitoraggio avanzamento)
# ---------------------------------------------------------------------------

setup: 
	${RSCRIPT} -e \
	'prj <- lbav2::prj$$new(id = "$(PRJ)", yt_id = "$(YT_ID)"); prj$$setup(chunks_len_mins = $(CHUNKS_LEN_MINS), trn_to_rev_ratio = $(TRN_TO_REV_RATIO))'


# ----------------------------------------------------------------------
# Sandbox
# ----------------------------------------------------------------------
# file di supporto per i sandbox: in questi vengono scritti i
# nomi di utenti github

edit-assign_sandbox:
	$(RM) /tmp/assign_sandbox && $(EDITOR) /tmp/assign_sandbox

edit-assign_rev1_sandbox:
	$(RM) /tmp/assign_rev1_sandbox && $(EDITOR) /tmp/assign_rev1_sandbox

edit-sandbox:
	$(RM) /tmp/assign_sandbox /tmp/assign_rev1_sandbox && \
	$(EDITOR) 	\
	/tmp/assign_sandbox \
	/tmp/assign_rev1_sandbox 

sandbox:
	${RSCRIPT} -e \
	'prj <- lbav2::prj$$new(id = "$(PRJ)", yt_id = "$(YT_ID)"); prj$$create_sandbox(sandbox_f = "/tmp/assign_sandbox", rev1_sandbox_f = "/tmp/assign_rev1_sandbox")'

# ----------------------------------------------------------------------
# Assign
# ----------------------------------------------------------------------
# file di supporto per i sandbox: in questi vengono scritti i
# nomi di utenti github

edit-assign_translate:
	$(RM) /tmp/assign_translate && $(EDITOR) /tmp/assign_translate

edit-assign_revise2:
	$(RM) /tmp/assign_revise2 && $(EDITOR) /tmp/assign_revise2

edit-assign:
	$(RM) /tmp/assign_translate /tmp/assign_revise2 && \
	$(EDITOR) 	\
	/tmp/assign_translate \
	/tmp/assign_revise2

assign:
	${RSCRIPT} -e \
	'prj <- lbav2::prj$$new(id = "$(PRJ)", yt_id = "$(YT_ID)"); prj$$assign(translate_f = "/tmp/assign_translate", revise2_f = "/tmp/assign_revise2")'


# --------------------------------------------
# Target per assegnare e markare completamenti
# --------------------------------------------

# file di supporto per markare gli avanzamenti: IN QUESTI VANNO SCRITTI I FILE
# NELLA VERSIONE subs_000000.srt o revs_000000_000500.srt (che sono quelli
# che si hanno dalla chat telegram
edit-mark_trn_completed:
	$(RM)    /tmp/mark_trn_completed && \
	$(EDITOR) /tmp/mark_trn_completed

edit-mark_rev1_started:
	$(RM)    /tmp/mark_rev1_started && \
	$(EDITOR) /tmp/mark_rev1_started

edit-mark_rev1_completed:
	$(RM)    /tmp/mark_rev1_completed && \
	$(EDITOR) /tmp/mark_rev1_completed

edit-mark_rev2_completed:
	$(RM)    /tmp/mark_rev2_completed && \
	$(EDITOR) /tmp/mark_rev2_completed

edit-mark:
	$(RM) /tmp/mark_* && \
	$(EDITOR) \
	/tmp/mark_trn_completed  \
	/tmp/mark_rev1_started   \
	/tmp/mark_rev1_completed \
	/tmp/mark_rev2_completed 

# per markare un file come tradotto o rev completata (in seguito a
# una comunicazione in chat telegram da parte di traduttori o revisori)
# evolve il vecchio mark as completed
mark_progresses:
	${R} < \
	'prj <- lbav2::prj$$new(id = "$(PRJ)", yt_id = "$(YT_ID)"); prj$$mark_progresses(trn_completed_f = "/tmp/mark_trn_completed", rev1_started_f = "/tmp/mark_rev1_started", rev1_completed_f = "/tmp/mark_rev1_completed",rev2_completed_f = "/tmp/mark_rev2_completed")' 
	# ${RSCRIPT} -e \



# ------------
# Misc & utils
# ------------
monitoring:
	${RSCRIPT} -e \
	'lbav2::prj$$new(id = "$(PRJ)", yt_id = "$(YT_ID)")$$monitoring()'

git-log-analysis:
	${RSCRIPT} -e \
	'lbav2::prj$$new(id = "$(PRJ)", yt_id = "$(YT_ID)")$$git_log_analysis()'

# mplayer the video with subs
view-with-source-subs:
	mplayer --sub-file=source/$(PRJ).srt video/$(PRJ).mp4 

# make a version of the video with subs (english, for translation)
burn-translate-with-subs:
	ffmpeg -i source/$(PRJ).srt /tmp/$(PRJ).ass && \
	ffmpeg -i video/$(PRJ).mp4 -vf ass=/tmp/$(PRJ).ass \
	/tmp/$(PRJ)_en_subtitled.mp4

# make a version of the video with subs (english, for translation)
burn-revise-with-subs:
	cat subs/$(PRJ)/revs_*.srt > /tmp/$(PRJ)_revs.srt && \
	ffmpeg -i /tmp/$(PRJ)_revs.srt /tmp/$(PRJ)_revs.ass && \
	ffmpeg -i video/$(PRJ).mp4 -vf ass=/tmp/$(PRJ)_revs.ass \
	/tmp/$(PRJ)_it_for_revs.mp4

# prima linea solo video, seconda vari sub anche tradotti
download-video:
	cd /tmp && \
	youtube-dl -f 18 "https://www.youtube.com/watch?v=$(YT_ID)"

download-subs:
	cd /tmp && \
	youtube-dl  --skip-download --all-subs "https://www.youtube.com/watch?v=$(YT_ID)"


# ------------
# Final srt
# ------------

final-srt:
	${RSCRIPT} -e \
	'lbav2::prj$$new(id = "$(PRJ)", yt_id = "$(YT_ID)")$$make_final_srt()'	2>&1 | less

final-srt-stats:
	${RSCRIPT} -e \
	'lbav2::prj$$new(id = "$(PRJ)", yt_id = "$(YT_ID)")$$final_srt_stats()'

view-with-final-subs:
	mplayer --sub-file=subs/$(PRJ)/$(PRJ)_final.srt video/$(PRJ).mp4 

edit-final-subs:
	$(SUBEDITOR) subs/$(PRJ)/$(PRJ)_final.srt video/$(PRJ).mp4

view-final-subs:
	less subs/$(PRJ)/$(PRJ)_final.srt

# ------------
# Help
# ------------
help:
	@echo "====="
	@echo "Usage"
	@echo "====="
	@echo
	@echo " make TARGET PRJ=subs_project"
	@echo
	@echo " con PRJ cartella sotto subs, di default 'test'"
	@echo
	@echo "-------------"
	@echo "Users targets"
	@echo "-------------"
	@echo
	@echo " edit-users-db      - edit users data"
	@echo " list-users         - list users and permissions"
	@echo " summon-revisors    - list revisors with @ for easy telegram copy'n paste"
	@echo
	@echo "-----------"
	@echo "Subs source "
	@echo "-----------"
	@echo
	@echo " split-source-subs  - split original source subs for translation"
	@echo
	@echo "   es: make split-source-subs YT_ID=cJ9kGZMbyVw"
	@echo "   es: make split-source-subs PRJ=hnva2 YT_ID=cJ9kGZMbyVw"
	@echo
	@echo "--------------------------------"
	@echo "Assignments (sandbox, translate) "
	@echo "--------------------------------"
	@echo
	@echo " edit-assign-files   - create/edit /tmp/sandbox and /tmp/translate"
	@echo " assign              - create sandboxes or assign translates"
	@echo "                       using /tmp/sandbox and /tmp/translate"
	@echo
	@echo "--------------------------------"
	@echo "Assignments (sandbox, translate) "
	@echo "--------------------------------"
	@echo
	@echo " edit-completed-files   - create/edit /tmp/completed_files"
	@echo " mark-as-completed      - mark file as completed using /tmp/completed_files"
	@echo "                          check for available revisions and summon revisors"
	@echo
	@echo "-----"
	@echo "Utils"
	@echo "-----"
	@echo
	@echo " monitoring                 - plot advancement status"
	@echo " git-log-analysis           - analyze git logs with gitinspector"
	@echo " view-with-subs             - mpv the video with subs from source"
	@echo " burn-with-subs             - burn the subs into the video (output in /tmp)"
	@echo 
	@echo "----------------"
	@echo "Useful variables"
	@echo "----------------"
	@echo
	@echo " PRJ                 - project name"
	@echo " YT_ID               - YouTube id of the video"
	@echo " CHUNKS_LEN_MINS     - minutes (length) for subs-chunks splitting (default = 5mins)"
	@echo " TRN_TO_REV_RATIO    - how much subs for a rev (default = 4)"
	@echo

