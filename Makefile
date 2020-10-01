TARGETS=SimpleApp RddApp

$(TARGETS):
	spark-submit --master 'local[4]' $@.py

.PHONY: $(TARGETS)
