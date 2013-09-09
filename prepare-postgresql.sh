sudo -u postgres createuser --pwprompt --superuser matcher
sudo -u postgres createdb -E UNICODE -O matcher matcher
sudo -u postgres createdb -E UNICODE -O matcher test_matcher
